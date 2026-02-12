MOVE_SYMBOLS = {
    "pull": "↑",
    "bump": "⇡",
    "dynamic": "▲",
    "match": "≡",
    "high_foot": "┐",
    "heel_hook": "⟂",
    "drop_knee": "⤵"
}

HOLD_SYMBOLS = {
    "crimp": "▭",
    "sloper": "◜",
    "pinch": "⧖",
    "jug": "◯",
    "volume": "⬒"
}


def compile_symbols(sequence):

    compiled = []

    for step in sequence:

        move = step["move"].lower()
        hold = step["hold"].lower()

        compiled.append({
            "move_symbol": MOVE_SYMBOLS.get(move, "?"),
            "hold_symbol": HOLD_SYMBOLS.get(hold, "?"),
            "raw": step
        })

    return compiled
