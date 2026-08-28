#!/usr/bin/env python3
"""Animate approved still keyframes into short editorial-motion clips.

Hybrid production method: stills + slow push-ins / pans / grain / vignette,
as described in the project README ("Editorial Plan"). Output is 16:9 H.264
with a silent stereo track so clips drop cleanly into the timeline.

Usage:
    python scripts/utilities/animate_stills.py [--all]

Defaults to rendering the six missing hero shots for "Baby Batter for
Breakfast". Each entry maps to a timed shot plan ID.
"""

import argparse
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

try:
    import imageio_ffmpeg

    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # pragma: no cover - fallback to PATH
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

FPS = 24
WIDTH, HEIGHT = 1920, 1080

# (shot id, source still, output clip, duration s, motion)
SHOTS = [
    (
        "V001",
        "generations/stills/candidates/V001_singer-wakes_v001.png",
        "V001_singer-wakes.mp4",
        4.5,
        "push_in",
    ),
    (
        "V002",
        "generations/stills/candidates/V002_cowboy-turn_v001.png",
        "V002_cowboy-turn.mp4",
        4.5,
        "push_in",
    ),
    (
        "V006",
        "generations/stills/candidates/V006_couple-stir-together_v001.png",
        "V006_couple-stir-together.mp4",
        5.5,
        "push_in",
    ),
    (
        "V007",
        "generations/stills/candidates/V007_waffle-flip_v001.png",
        "V007_waffle-flip.mp4",
        4.0,
        "push_in_strong",
    ),
    (
        "V008",
        "generations/stills/candidates/V008_flour-dance-finale_v001.png",
        "V008_flour-dance-finale.mp4",
        5.5,
        "push_in_strong",
    ),
    (
        "V009",
        "generations/stills/candidates/V009_product-box_v001.png",
        "V009_product-box.mp4",
        5.0,
        "pan_lr",
    ),
    (
        "V010",
        "generations/stills/candidates/V010_thumbs-up_v001.png",
        "V010_thumbs-up.mp4",
        4.5,
        "push_in_gentle",
    ),
]

# zoompan motion templates (on = output frame counter, d = frames per input)
MOTION = {
    "push_in": "z='min(1.001+0.00065*on,1.075)':x='iw/2-(iw/zoom)/2':y='ih/2-(ih/zoom)/2'",
    "push_in_gentle": "z='min(1.001+0.00045*on,1.055)':x='iw/2-(iw/zoom)/2':y='ih/2-(ih/zoom)/2'",
    "push_in_strong": "z='min(1.002+0.0010*on,1.10)':x='iw/2-(iw/zoom)/2':y='ih/2-(ih/zoom)/2'",
}

# Pan template uses the literal frame count (d is not available in x/y).
def pan_lr(frames: int) -> str:
    return (
        f"z='1.085':x='(iw-iw/zoom)*(on/{frames - 1})'"
        f":y='ih/2-(ih/zoom)/2'"
    )


MOTION_BUILDERS = {
    "push_in": lambda frames: MOTION["push_in"],
    "push_in_gentle": lambda frames: MOTION["push_in_gentle"],
    "push_in_strong": lambda frames: MOTION["push_in_strong"],
    "pan_lr": pan_lr,
}


def build_filter(motion: str, frames: int) -> str:
    zoom = MOTION_BUILDERS[motion](frames)
    # Crop source to 16:9, upscale for headroom, zoompan to target, then grade.
    return (
        f"crop=ih*16/9:ih,scale=2880:1620:flags=lanczos,"
        f"zoompan={zoom}:d={frames}:s={WIDTH}x{HEIGHT}:fps={FPS},"
        f"setsar=1,"
        f"vignette=PI/4.8,"
        f"eq=contrast=1.03:saturation=1.04,"
        f"noise=alls=5:allf=t+u,"
        f"format=yuv420p"
    )


def render(shot_id: str, src: Path, out: Path, duration: float, motion: str) -> None:
    frames = max(2, round(duration * FPS))
    vf = build_filter(motion, frames)
    cmd = [
        FFMPEG,
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-loop",
        "1",
        "-i",
        str(src),
        "-f",
        "lavfi",
        "-i",
        "anullsrc=r=48000:cl=stereo",
        "-vf",
        vf,
        "-t",
        f"{duration:.3f}",
        "-r",
        str(FPS),
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "20",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-movflags",
        "+faststart",
        "-shortest",
        str(out),
    ]
    print(f"[{shot_id}] {out.name} ({duration}s, {motion}) ...")
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="render every shot entry")
    args = parser.parse_args()

    for shot_id, rel_src, rel_out, duration, motion in SHOTS:
        src = ROOT / rel_src
        out = ROOT / rel_out
        if not src.exists():
            print(f"[{shot_id}] SKIP missing source: {src}")
            continue
        if out.exists() and not args.all:
            print(f"[{shot_id}] SKIP exists: {out}")
            continue
        render(shot_id, src, out, duration, motion)
        print(f"[{shot_id}] DONE -> {out}")


if __name__ == "__main__":
    main()
