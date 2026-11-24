"""Entrypoint for the make.fun one-line cat joke competition.

Writes exactly one line — the joke — to the output directory as entry.txt.
Deterministic: no network, no randomness, nothing else in the file.
"""

import os

JOKE = "My cat filed a noise complaint — against me — for sleeping through the exact hour he chose to sprint."


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


main()
