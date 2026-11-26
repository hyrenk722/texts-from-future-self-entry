"""Texts From Your Future Self (u-motasimfuad-texts-from-your-future-self-dd44595e).

Writes one text message from the writer's future self to /output/entry.txt.
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""

import os
import sys

ENTRY_TEXT = "future you. the gym membership outlived the relationship. cancel one of them."

MAX_CHARS = 200


def check_gate(text):
    """Return True when text satisfies the competition gate."""
    if not isinstance(text, str):
        return False
    if len(text) < 1 or len(text) > MAX_CHARS:
        return False
    if not text.strip():
        return False
    text.encode("utf-8")
    return True


def main():
    if not check_gate(ENTRY_TEXT):
        print("gate failed: entry text does not satisfy 1-200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    with open(out_path, "rb") as f:
        written = f.read()
    if written != ENTRY_TEXT.encode("utf-8"):
        print("verify failed: written bytes do not match entry text", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(ENTRY_TEXT)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
