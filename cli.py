import json
import sys
from core.compile_trace import compile_video
from render.build_artifact import build_svg


def main(video_path):
    output_json = "output.sequence.log.json"
    output_svg = "output.svg"

    artifact = compile_video(video_path, output_json)
    build_svg(artifact, output_svg)

    print("STACKTRACE prototype complete")
    print("Generated:", output_json, output_svg)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python cli.py <video>")
        sys.exit(1)

    main(sys.argv[1])
