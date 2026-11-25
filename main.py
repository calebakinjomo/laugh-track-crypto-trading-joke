"""Write one crypto-trading joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
The output directory is created first if it does not exist, so the entry
lands even on a fresh sandbox. The entry itself is fixed: a single
119-character joke about buying the dip, written verbatim plus a newline.
"""

import os

LINE = (
    "I bought the dip, then the dip dipped, then the dip's dip dipped "
    "— my portfolio is now a Russian doll of bad decisions."
)

if len(LINE) != 119 or "\n" in LINE or "\r" in LINE:
    raise ValueError("entry must be a single 119-character line")

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write(LINE + "\n")
