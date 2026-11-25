"""Write one crypto-trading joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "I bought the dip, then the dip dipped, then the dip's dip dipped "
    "— my portfolio is now a Russian doll of bad decisions."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
