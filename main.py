#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to /output/entry.txt: a small, concrete scene
meant to relax the reader by showing rather than instructing.
Standard library only, no network, no input.
"""

import os

TEXT = "Somewhere a kettle has just boiled, and nobody is in a hurry to pour it. Rain threads the window, slow as handwriting. The room keeps its warm corner of light, the chair keeps the shape of you, and every small sound arrives already forgiven."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
