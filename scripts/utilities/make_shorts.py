#!/usr/bin/env python3
"""Build vertical (1080x1920) social shorts from the flat clips.

- Blur-pad each 16:9 clip into a 9:16 frame (motion preserved in the center).
- Concatenate the selected beats for each short.
- Underscore with a section of the project song (fade in/out).
- Add a hand-built end card (created with Pillow, not AI text) that
  promotes @plaguedr.online.
- Optional title overlay at the head of the short.

Outputs land in renders/review/ as 1080x1920 H.264 + AAC.
"""

import shutil
import subprocess
from pathlib import Path

try:
    import imageio_ffmpeg

    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # pragma: no cover
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

ROOT = Path(__file__).resolve().parents[2]
SONG = ROOT / "assets/audio/belgium-waffles-and-babybatter_clean.mp3"
SCRATCH = ROOT / "scratch" / "shorts"
OUT = ROOT / "renders" / "review"

FPS = 24
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# (source clip, start offset after head trim, duration to use)
SHORT_1 = {
    "name": "baby-batter_fb-short-01",
    "title": "BABY BATTER FOR BREAKFAST",
    "audio_start": 17.0,
    "clips": [
        ("V001_singer-wakes.mp4", 0.3, 4.0),
        ("V002_cowboy-turn.mp4", 0.3, 4.0),
        ("waffle-batter-pour.mp4", 0.3, 4.0),
        ("country-singer-whisk-jingle.mp4", 0.3, 4.0),
        ("waffle-batter-pour-fast.mp4", 0.3, 4.0),
        ("V007_waffle-flip.mp4", 0.3, 3.7),
        ("V008_flour-dance-finale.mp4", 0.3, 5.2),
        ("ENDCARD", 0.0, 4.0),
    ],
}

SHORT_2 = {
    "name": "baby-batter_fb-short-02",
    "title": "THE SECRET RECIPE",
    "audio_start": 97.0,
    "clips": [
        ("cowboy-breakfast-mixing.mp4", 0.3, 4.0),
        ("waffle-extras-pushed-aside.mp4", 0.3, 4.0),
        ("V006_couple-stir-together.mp4", 0.3, 5.0),
        ("V009_product-box.mp4", 0.3, 4.6),
        ("V010_thumbs-up.mp4", 0.3, 4.2),
        ("V008_flour-dance-finale.mp4", 0.3, 5.0),
        ("ENDCARD", 0.0, 4.0),
    ],
}

SHORTS = [SHORT_1, SHORT_2]


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        [FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True
    ).stderr
    for line in out.splitlines():
        if "Duration:" in line:
            t = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = t.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"could not probe {path}")


def verticalize(src: Path, out: Path, dur: float) -> None:
    """16:9 -> 9:16 blur-pad, keep center motion, silent audio for concat."""
    vf = (
        "[0:v]split=2[bg][fg];"
        "[bg]scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920,boxblur=24:2,eq=brightness=-0.10:saturation=0.85[bgv];"
        "[fg]scale=1080:-2[fgs];"
        "[bgv][fgs]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[v]"
    )
    cmd = [
        FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
        "-ss", "0", "-i", str(src),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-filter_complex", vf,
        "-map", "[v]", "-map", "1:a",
        "-t", f"{dur:.3f}",
        "-r", str(FPS),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "128k",
        str(out),
    ]
    subprocess.run(cmd, check=True)


def concat_files(files: list[Path], out: Path) -> None:
    lst = SCRATCH / "concat.txt"
    lst.write_text("".join(f"file '{f.as_posix()}'\n" for f in files))
    cmd = [
        FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(lst),
        "-c", "copy", str(out),
    ]
    subprocess.run(cmd, check=True)


def make_title_png(short: dict) -> Path:
    """Render a clean title overlay (Pillow, no AI text) with alpha."""
    from PIL import Image, ImageDraw, ImageFont

    path = SCRATCH / f"{short['name']}_title.png"
    if path.exists():
        return path

    W, H = 1080, 260
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)

    # semi-transparent backing plate
    d.rounded_rectangle([40, 30, W - 40, H - 30], radius=24, fill=(20, 14, 10, 150), outline=(233, 205, 160, 220), width=3)

    text = short["title"]
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    if tw > W - 120:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(64 * (W - 140) / tw))
        bbox = d.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((W - tw) / 2 - bbox[0], (H - th) / 2 - bbox[1]), text, font=font, fill=(240, 226, 199, 255))
    img.save(path)
    return path


def finish(concat: Path, short: dict, out: Path) -> None:
    """Two-pass finish: (1) encode video + title overlay, (2) copy-mux audio.

    Doing both in one ffmpeg pass with a -ss/-t audio input produced a
    corrupt H.264 stream in the bundled build, so we keep them separate.
    """
    dur = sum(c[2] for c in short["clips"])
    title = make_title_png(short)
    video_only = SCRATCH / f"{short['name']}_videoonly.mp4"

    # Pass 1: video with title overlay and fades, no audio.
    fc = (
        f"[0:v]fade=t=in:st=0:d=0.5,fade=t=out:st={dur - 1.3:.2f}:d=1.3,format=yuv420p[base];"
        "[1:v]format=rgba,"
        "fade=t=in:st=0:d=0.4:alpha=1,"
        "fade=t=out:st=2.6:d=0.6:alpha=1[title];"
        "[base][title]overlay=(W-w)/2:y=160:eof_action=pass,format=yuv420p[v]"
    )
    subprocess.run(
        [
            FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
            "-i", str(concat),
            "-loop", "1", "-i", str(title),
            "-filter_complex", fc,
            "-map", "[v]",
            "-r", str(FPS),
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-t", f"{dur:.3f}",
            str(video_only),
        ],
        check=True,
    )

    # Pass 2: audio fades from the clean song, stream-copy the video.
    subprocess.run(
        [
            FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
            "-ss", f"{short['audio_start']:.2f}", "-t", f"{dur:.3f}", "-i", str(SONG),
            "-i", str(video_only),
            "-filter_complex",
            f"[0:a]afade=t=in:st=0:d=0.8,afade=t=out:st={dur - 1.5:.2f}:d=1.5[a]",
            "-map", "[a]", "-map", "1:v",
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart",
            "-t", f"{dur:.3f}",
            str(out),
        ],
        check=True,
    )


def main() -> None:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    for short in SHORTS:
        parts: list[Path] = []
        for i, (name, head, dur) in enumerate(short["clips"]):
            if name == "ENDCARD":
                src = ROOT / "project-files" / "graphics" / "ENDCARD_social_v001.png"
                tmp = SCRATCH / f"{short['name']}_{i:02d}_endcard.mp4"
                if not tmp.exists():
                    vf = "scale=1080:1920,format=yuv420p"
                    subprocess.run(
                        [
                            FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                            "-loop", "1", "-i", str(src),
                            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                            "-vf", vf, "-t", f"{dur:.3f}", "-r", str(FPS),
                            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                            "-c:a", "aac", "-b:a", "128k", str(tmp),
                        ],
                        check=True,
                    )
            else:
                src = ROOT / name
                tmp = SCRATCH / f"{short['name']}_{i:02d}_{Path(name).stem}.mp4"
                if not tmp.exists():
                    verticalize(src, tmp, dur)
            parts.append(tmp)

        concat = SCRATCH / f"{short['name']}_concat.mp4"
        concat_files(parts, concat)

        final = OUT / f"{short['name']}_1080x1920.mp4"
        finish(concat, short, final)
        print(f"DONE {final} ({probe_duration(final):.1f}s)")


if __name__ == "__main__":
    main()
