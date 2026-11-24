# one-line-cat-joke

Entry for make.fun competition [u-aldy998-the-one-line-cat-joke-that-lands-a7b18262](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262) — one joke about cats, a single line, under 200 characters, nothing else.

## The joke

> My cat filed a noise complaint — against me — for sleeping through the exact hour he chose to sprint.

## How it works

`main.py` writes that single line to the output directory as `entry.txt`. Deterministic: no network, no randomness, no side effects.

## Files

- `main.py` — entrypoint: writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
- `LICENSE` — MIT.
