# stacktrace
Climbing movement compiler + visual artifact generator.

STACKTRACE analyzes climbing videos and produces:
- route trace geometry
- movement sequence instructions
- symbolic micrographics output
- printable design artifacts (SVG)

Primary Output Engine: SEQUENCE.LOG

---

## core idea
Treat climbing as executable logic.

video → pose/motion analysis → symbolic sequence → visual artifact

Each climb compiles into:
- route trace
- ordered movement operators
- hold classifications
- microtext annotations
- printable design layout

---

## current prototype
- CLI compiler scaffold
- fake trace generator
- fake movement instruction set
- SEQUENCE.LOG schema
- SVG artifact renderer

This version demonstrates architecture + pipeline.

---

## architecture

core/
    compile_trace.py
    compiler + trace engine

render/
    build_artifact.py
    svg layout generator

sequence_log/
    schema + artifact examples

cli.py
    entry point pipeline

---

## techstack

Language:
- Python

Core Libraries:
- OpenCV (future CV analysis)
- NumPy
- svgwrite

Future Additions:
- MediaPipe (pose detection)
- PyTorch (movement classification)
- FastAPI (API layer)
- Tauri or Electron (desktop shell)
- React Native or Flutter (mobile companion)

---

## roadmap

Phase 1:
✔ prototype compiler
✔ svg artifact renderer

Phase 2:
- pose detection
- center-of-mass tracking
- hold detection
- move segmentation

Phase 3:
- desktop interface
- mobile capture companion
- printable shirt generator

---

## run prototype

create venv:

mac/linux:
python3 -m venv .venv
source .venv/bin/activate

windows:
python -m venv .venv
.venv\\Scripts\\Activate.ps1

install deps:
pip install -r requirements.txt

run compiler:
python cli.py examples/sample_video.mp4

outputs:
output.sequence.log.json
output.svg
