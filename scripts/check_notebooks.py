"""Fail if any non-empty .ipynb file isn't valid JSON (catches a corrupted save)."""
import glob
import json
import os
import sys

bad = []
for f in glob.glob("**/*.ipynb", recursive=True):
    if os.path.getsize(f) == 0:
        continue  # placeholder notebooks are fine, just not corrupted ones
    try:
        json.load(open(f, encoding="utf-8"))
    except Exception as e:
        bad.append((f, str(e)))

for f, e in bad:
    print(f"BAD: {f}: {e}")

if bad:
    sys.exit(1)
print(f"OK: all non-empty notebooks are valid JSON")
