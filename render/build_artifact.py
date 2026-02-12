import svgwrite
from core.symbol_engine import compile_symbols


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 600

# --------------------------------------------------
# LAYOUT CONSTANTS
# --------------------------------------------------

SEQ_X = 220
SEQ_Y = 200
SEQ_W = 160
SEQ_H = 340


def build_svg(sequence_log, output_svg):

    dwg = svgwrite.Drawing(
        output_svg,
        size=(f"{CANVAS_WIDTH}px", f"{CANVAS_HEIGHT}px")
    )

    dwg.attribs["font-family"] = "monospace"
    dwg.attribs["font-size"] = "10px"
    dwg.attribs["fill"] = "black"

    # --------------------------------------------------
    # ROUTE TRACE PANEL (LEFT)
    # --------------------------------------------------

    trace_points = [
        (p["x"], p["y"])
        for p in sequence_log["trace"]
    ]

    # faint guide grid lines
    for x in [80, 140, 200]:
        dwg.add(
            dwg.line(
                start=(x, 0),
                end=(x, CANVAS_HEIGHT),
                stroke="black",
                stroke_width=0.5,
                opacity=0.3
            )
        )

    # route polyline
    dwg.add(
        dwg.polyline(
            trace_points,
            stroke="black",
            fill="none",
            stroke_width=2
        )
    )

    # joints
    for pt in trace_points:
        dwg.add(
            dwg.circle(
                center=pt,
                r=3,
                fill="black"
            )
        )

    # --------------------------------------------------
    # DASHBOARD BOX (TOP RIGHT)
    # --------------------------------------------------

    dash_x = 220
    dash_y = 60
    dash_w = 160
    dash_h = 110

    dwg.add(
        dwg.rect(
            insert=(dash_x, dash_y),
            size=(dash_w, dash_h),
            fill="none",
            stroke="black",
            stroke_width=1.5
        )
    )

    meta = [
        ("DIFFICULTY", sequence_log.get("grade", "UNKNOWN")),
        ("LOCATION", sequence_log.get("location", "UNKNOWN")),
        ("STATUS", "SENT")
    ]

    ty = dash_y + 25
    for label, value in meta:
        dwg.add(
            dwg.text(
                label,
                insert=(dash_x + 10, ty),
                fill="black",
                font_size="10px"
            )
        )
        dwg.add(
            dwg.text(
                value,
                insert=(dash_x + 90, ty),
                fill="black",
                font_size="10px"
            )
        )
        ty += 25

    # --------------------------------------------------
    # SEQUENCE BOX
    # --------------------------------------------------

    seq_x = SEQ_X
    seq_y = SEQ_Y
    seq_w = SEQ_W
    seq_h = SEQ_H

    # outer box
    dwg.add(
        dwg.rect(
            insert=(seq_x, seq_y),
            size=(seq_w, seq_h),
            fill="none",
            stroke="black",
            stroke_width=1.5
        )
    )

    compiled = compile_symbols(sequence_log["sequence"])

    # layout settings
    padding_x = 12
    padding_y = 20

    cell_w = 28
    cell_h = 64

    start_x = seq_x + padding_x
    start_y = seq_y + padding_y

    max_cols = max(1, int((seq_w - padding_x * 2) / cell_w))

    for i, step in enumerate(compiled):

        col = i % max_cols
        row = i // max_cols

        gx = start_x + col * cell_w
        gy = start_y + row * cell_h

        # movement symbol
        dwg.add(
            dwg.text(
                step["move_symbol"],
                insert=(gx, gy),
                fill="black",
                font_size="14px"
            )
        )

        # hold symbol
        dwg.add(
            dwg.text(
                step["hold_symbol"],
                insert=(gx, gy + 16),
                fill="black",
                font_size="14px"
            )
        )

        raw = step["raw"]

        seq_label = f'SEQ_{i+1:02d}'
        move_label = raw["move"].upper()
        state_label = raw.get("state", "EXEC").upper()

        # seq id
        dwg.add(
            dwg.text(
                seq_label,
                insert=(gx - 2, gy + 28),
                fill="black",
                font_size="6px"
            )
        )

        # movement label
        dwg.add(
            dwg.text(
                move_label,
                insert=(gx - 2, gy + 36),
                fill="black",
                font_size="6px"
            )
        )

        # state / execution label
        dwg.add(
            dwg.text(
                state_label,
                insert=(gx - 2, gy + 44),
                fill="black",
                font_size="6px"
            )
        )


    # faint vertical micro grid
    for gx in range(int(seq_x), int(seq_x + seq_w), 14):
        dwg.add(
            dwg.line(
                start=(gx, seq_y),
                end=(gx, seq_y + seq_h),
                stroke="black",
                stroke_width=0.3,
                opacity=0.15
            )
        )

    # --------------------------------------------------
    # SAVE SVG
    # --------------------------------------------------

    dwg.save()
