#!/usr/bin/env python3
"""Assemble the full-length 'Baby Batter for Breakfast' music video (rough cut).

Follows docs/TIMED_SHOT_PLAN.md. Each shot is rendered to a uniform
1920x1080@24fps segment, concatenated, then muxed with the clean song master.

Stills get editorial motion (zoompan push-ins / pans + grain). Video clips
are trimmed to their slot (or gently slowed when the slot is longer than the
source). Missing dedicated keyframes fall back to close-match placeholders and
are listed at the end; swap them in via STILLS/VIDEOS once approved.

Output: renders/review/baby-batter_full_1080p_v001.mp4
"""

import shutil
import subprocess
from pathlib import Path

try:
    import imageio_ffmpeg

    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

ROOT = Path(__file__).resolve().parents[2]
STILLS = ROOT / "generations/stills/candidates"
SCRATCH = ROOT / "scratch" / "full_length"
OUT = ROOT / "renders/review/baby-batter_full_1080p_v001.mp4"
SONG = ROOT / "assets/audio/belgium-waffles-and-babybatter_clean.mp3"

FPS = 24
W, H = 1920, 1080

# id, in, out, kind, source, notes
SHOTS = [
    ("S001", 0.00, 3.00, "still", "S001_farmhouse-sunrise_v001.png", ""),
    ("S002", 3.00, 6.10, "still", "LOC_farmhouse-kitchen-wide_v001.png", "empty kitchen"),
    ("V001", 6.10, 9.80, "video", "V001_singer-wakes.mp4", ""),
    ("S003", 9.80, 12.50, "still", "S003_cowboy-boots_v001.png", ""),
    ("V002", 12.50, 14.60, "video", "V002_cowboy-turn.mp4", ""),
    ("S004", 14.60, 17.70, "still", "S004_bacon-ham-rejected_v001.png", ""),
    ("S005", 17.70, 19.54, "still", "S005_mixing-bowl-reveal_v001.png", ""),
    ("V003", 19.54, 23.13, "video", "waffle-batter-pour.mp4", ""),
    ("S006", 23.13, 26.26, "still", "S006_finished-waffle-hero_v001.png", ""),
    ("V004", 26.26, 29.74, "video", "country-singer-whisk-jingle.mp4", ""),
    ("S007", 29.74, 33.73, "still", "S007_waffle-stack-montage_v001.png", ""),
    ("S008", 33.73, 36.50, "still", "S008_steam-flour-wipe_v001.png", ""),
    ("S009", 36.50, 39.33, "still", "S009_singer-enters-kitchen_v001.png", ""),
    ("V005", 39.33, 42.86, "video", "waffle-extras-pushed-aside.mp4", ""),
    ("S010", 42.86, 46.73, "video", "cowboy-breakfast-mixing.mp4", "ph: singer-admire beat"),
    ("S011", 46.80, 50.80, "still", "S011_singer-testimonial_v001.png", ""),
    ("S012", 50.80, 52.80, "still", "S012_flour-on-nose_v001.png", ""),
    ("V003B", 52.80, 56.42, "video", "waffle-batter-pour-fast.mp4", ""),
    ("S013", 56.42, 60.36, "still", "S007_waffle-stack-montage_v001.png", "reuse: lunch tableau"),
    ("S014", 60.36, 63.09, "still", "LOC_farmhouse-kitchen-wide_v001.png", "DARKWARM: supper tableau"),
    ("S015", 63.09, 66.80, "video", "waffle-extras-pushed-aside.mp4", "ph: milk-glass toast"),
    ("V005B", 66.80, 73.03, "video", "waffle-extras-pushed-aside.mp4", "REUSE:"),
    ("S016", 73.03, 77.46, "video", "cowboy-breakfast-mixing.mp4", "REUSE: fans-with-recipe beat"),
    ("S017", 77.46, 80.57, "still", "S005_mixing-bowl-reveal_v001.png", "reuse: batter texture"),
    ("S018", 80.57, 83.50, "still", "S008_steam-flour-wipe_v001.png", "reuse: romantic shift"),
    ("S019", 83.50, 86.57, "still", "S005_mixing-bowl-reveal_v001.png", "reuse: hands to whisk"),
    ("S020", 86.57, 88.23, "still", "S005_mixing-bowl-reveal_v001.png", "reuse: slow whisk"),
    ("S021", 88.23, 92.97, "still", "S005_mixing-bowl-reveal_v001.png", "reuse: thick batter"),
    ("V006", 92.97, 99.53, "video", "V006_couple-stir-together.mp4", "SLOW:6.56"),
    ("S022", 99.53, 101.37, "still", "S005_mixing-bowl-reveal_v001.png", "reuse: bowl pickup"),
    ("V008", 101.37, 107.04, "video", "V008_flour-dance-finale.mp4", "SLOW:5.67"),
    ("V007", 107.04, 110.50, "video", "V007_waffle-flip.mp4", ""),
    ("S023", 110.50, 113.77, "still", "S006_finished-waffle-hero_v001.png", "reuse: waffle stack"),
    ("V009", 113.77, 118.90, "video", "V009_product-box.mp4", ""),
    ("G001", 118.90, 123.43, "still", "V009_product-box_labelled_v001.png", "LABEL: after a delay? no—insert at slot"),
    ("V010", 123.43, 126.50, "video", "V010_thumbs-up.mp4", ""),
    ("S024", 126.50, 132.37, "still", "ENDCARD_wide_v001.png", "end card hold"),
]


def probe(path: Path) -> float:
    out = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    for line in out.splitlines():
        if "Duration:" in line:
            t = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = t.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"probe failed: {path}")


def make_wide_endcard() -> Path:
    """16:9 variant of the social end card (Pillow, no AI text)."""
    from PIL import Image, ImageDraw, ImageFont

    path = STILLS / "ENDCARD_wide_v001.png"
    if path.exists():
        return path
    W, H = 1920, 1080
    img = Image.new("RGB", (W, H), (48, 30, 20))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(48 - 26 * t), int(30 - 14 * t), int(20 - 8 * t)))
    FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    def center(txt, size, y, fill):
        f = ImageFont.truetype(FB, size)
        b = d.textbbox((0, 0), txt, font=f)
        d.text(((W - (b[2] - b[0])) / 2 - b[0], y), txt, font=f, fill=fill)
    center("BABY BATTER", 120, 200, (233, 205, 160))
    center("FOR BREAKFAST", 54, 340, (200, 166, 122))
    center("COME SEE MORE", 72, 480, (240, 226, 199))
    handle = "@plaguedr.online"
    f = ImageFont.truetype(FB, 96)
    b = d.textbbox((0, 0), handle, font=f)
    tw = b[2] - b[0]
    x0, y0, x1, y1 = (W - tw) / 2 - 50, 600, (W + tw) / 2 + 50, 740
    d.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=(178, 32, 34), outline=(230, 200, 160), width=5)
    d.text(((W - tw) / 2, y0 + 28), handle, font=f, fill=(255, 244, 220))
    center("waffles, biscuits or pie", 44, 850, (170, 140, 105))
    img.save(path)
    return path


def render_still(src: Path, out: Path, dur: float, motion: str, grain: int = 5) -> None:
    frames = max(2, round(dur * FPS))
    if motion == "pan":
        z = "z='1.09':x='(iw-iw/zoom)*(on/%d)':y='ih/2-(ih/zoom)/2'" % (frames - 1)
    else:
        z = "z='min(1.001+0.0007*on,1.08)':x='iw/2-(iw/zoom)/2':y='ih/2-(ih/zoom)/2'"
    vf = (
        f"crop=ih*16/9:ih,scale=2880:1620:flags=lanczos,"
        f"zoompan={z}:d={frames}:s={W}x{H}:fps={FPS},"
        "setsar=1,vignette=PI/4.8,eq=contrast=1.03:saturation=1.04,"
        f"noise=alls={grain}:allf=t+u,format=yuv420p"
    )
    subprocess.run([
        FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
        "-loop", "1", "-i", str(src),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-vf", vf, "-t", f"{dur:.3f}", "-r", str(FPS),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "128k", str(out),
    ], check=True)


def render_video(src: Path, out: Path, dur: float, offset: float = 0.3, slowto: float | None = None) -> None:
    if slowto and slowto > dur:
        rate = dur / slowto
        vf = f"setpts={rate:.6f}*PTS,scale={W}:{H}:flags=lanczos,setsar=1,format=yuv420p"
    else:
        vf = f"scale={W}:{H}:flags=lanczos,setsar=1,format=yuv420p"
    subprocess.run([
        FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
        "-ss", f"{offset:.2f}", "-i", str(src),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-vf", vf, "-t", f"{dur:.3f}", "-r", str(FPS),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "128k", str(out),
    ], check=True)


def main() -> None:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    make_wide_endcard()
    (SCRATCH / "concat.txt").write_text("")

    files = []
    for shot_id, t_in, t_out, kind, name, notes in SHOTS:
        dur = t_out - t_in
        out = SCRATCH / f"{shot_id}_{Path(name).stem}.mp4"
        if not out.exists():
            if kind == "still":
                src = STILLS / name
                motion = "pan" if shot_id in ("S004", "S015", "G001") else "push"
                grain = 5
                if "DARKWARM" in notes:
                    # darkened warm grade for the candlelit supper placeholder
                    subprocess.run([
                        FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                        "-loop", "1", "-i", str(src),
                        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                        "-vf", (
                            "crop=ih*16/9:ih,scale=2880:1620:flags=lanczos,"
                            f"zoompan=z='min(1.001+0.0007*on,1.08)':x='iw/2-(iw/zoom)/2':y='ih/2-(ih/zoom)/2':d={max(2,round(dur*FPS))}:s={W}x{H}:fps={FPS},"
                            "setsar=1,eq=brightness=-0.16:contrast=1.08:saturation=1.12:gamma=1.05,"
                            "vignette=PI/4.2,noise=alls=6:allf=t+u,format=yuv420p"
                        ),
                        "-t", f"{dur:.3f}", "-r", str(FPS),
                        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                        "-c:a", "aac", "-b:a", "128k", str(out),
                    ], check=True)
                else:
                    render_still(src, out, dur, motion, grain)
            else:
                src = ROOT / name
                offset = 0.3
                slowto = None
                if notes.startswith("SLOW:"):
                    slowto = float(notes.split(":")[1])
                render_video(src, out, dur, offset, slowto)
        files.append(out)
        print(f"  {shot_id} {dur:.2f}s")
        (SCRATCH / "concat.txt").write_text(
            (SCRATCH / "concat.txt").read_text() + f"file '{out.as_posix()}'\n"
        )

    concat = SCRATCH / "all_segments.mp4"
    subprocess.run([
        FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(SCRATCH / "concat.txt"),
        "-c", "copy", str(concat),
    ], check=True)

    vdur = probe(concat)
    # full song, small audio fade out at the very end
    end = min(vdur, probe(SONG)) - 1.8
    subprocess.run([
        FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(SONG), "-i", str(concat),
        "-filter_complex", f"[0:a]afade=t=out:st={end:.2f}:d=1.8[a]",
        "-map", "[a]", "-map", "1:v",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", str(OUT),
    ], check=True)
    print(f"DONE {OUT} ({probe(OUT):.2f}s)")


if __name__ == "__main__":
    main()
