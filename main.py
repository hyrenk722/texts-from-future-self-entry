"""Texts From Your Future Self -- entry program.

Writes the one-liner the writer's future self sends back, as plain
UTF-8 text, to entry.txt in the grader's output directory. Before
anything is written the line is put through the competition's gate:
it must be real text (not empty, not whitespace-only), no longer
than 200 characters, and encodable as UTF-8.
"""

import os
import sys

TEXT = "yes, you still rehearse arguments in the shower. no, you never win them."

MAX_LEN = 200


def check_text(line):
    """True when line clears every gate rule; False otherwise."""
    if not isinstance(line, str):
        return False
    if line.strip() == "":
        return False
    if len(line) > MAX_LEN:
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def verify_bytes(path, line):
    """True when the file at path holds exactly line as UTF-8 bytes."""
    with open(path, "rb") as handle:
        return handle.read() == line.encode("utf-8")


def emit(line, folder):
    """Drop line into entry.txt under folder; return the file path."""
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return path


def main():
    if not check_text(TEXT):
        print("gate failed: entry text does not pass the house gate", file=sys.stderr)
        return 1
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    path = emit(TEXT, folder)
    if not verify_bytes(path, TEXT):
        print("verify failed: entry.txt does not match the entry text", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
