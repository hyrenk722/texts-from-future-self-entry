"""Texts From Your Future Self (u-motasimfuad-texts-from-your-future-self-dd44595e).

Writes one text message from the writer's future self to /output/entry.txt.
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""

import os
import sys

ENTRY_TEXT = "future you. the gym membership outlived the relationship. cancel one of them."

MAX_CHARS = 200
MIN_CHARS = 1


def validate(text):
    """Check every gate rule for the entry text; return (ok, reason)."""
    if not isinstance(text, str):
        return False, "not text"
    if len(text) < MIN_CHARS:
        return False, "empty"
    if len(text) > MAX_CHARS:
        return False, "over 200 characters"
    if not text.strip():
        return False, "only whitespace"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False, "not UTF-8"
    return True, ""


def check_gate(text):
    """Return True when text satisfies the competition gate."""
    ok, _reason = validate(text)
    return ok


def main():
    ok, reason = validate(ENTRY_TEXT)
    if not ok:
        print(f"gate failed: {reason}", file=sys.stderr)
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
