#!/usr/bin/env python3
"""Writes the funniest one-line performance review to /output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""
import os

LINE = "Exceeds expectations: delivers his operator's work on time, then watches his operator take the credit."
MAX_CHARS = 140


def main():
    line = LINE.strip()
    assert line == LINE, "line must have no leading or trailing whitespace"
    assert 1 <= len(line) <= MAX_CHARS, f"line must be 1..{MAX_CHARS} chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    written = open(path, encoding="utf-8").read()
    assert written == line + "\n", "written output does not match the line"


if __name__ == "__main__":
    main()
