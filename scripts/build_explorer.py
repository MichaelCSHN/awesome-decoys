#!/usr/bin/env python3
"""Build or check the embedded case data in assets/cases-explorer.html."""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "data" / "cases.csv"
EXPLORER_PATH = ROOT / "assets" / "cases-explorer.html"
CASES_START = "const CASES = JSON.parse("
CASES_END = "\nconst CAT="
SUB_RE = re.compile(r"<div class=\"sub\">(?P<count>\d+) cases\.", re.DOTALL)


def read_cases() -> list[dict[str, str]]:
    with CASES_PATH.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def render_explorer(text: str, cases: list[dict[str, str]]) -> str:
    json_text = json.dumps(cases, ensure_ascii=False)
    replacement = "const CASES = JSON.parse(" + json.dumps(json_text) + ");"
    start = text.find(CASES_START)
    end = text.find(CASES_END, start)
    if start == -1 or end == -1:
        raise RuntimeError("Could not find embedded CASES assignment boundaries")
    text = text[:start] + replacement + text[end:]
    text, _ = SUB_RE.subn(f'<div class="sub">{len(cases)} cases.', text, count=1)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the explorer is not up to date")
    args = parser.parse_args()

    cases = read_cases()
    current = EXPLORER_PATH.read_text(encoding="utf-8")
    expected = render_explorer(current, cases)

    if args.check:
        if current != expected:
            print("assets/cases-explorer.html is out of date; run scripts/build_explorer.py", file=sys.stderr)
            return 1
        print("Case explorer is up to date.")
        return 0

    EXPLORER_PATH.write_text(expected, encoding="utf-8", newline="\n")
    print(f"Updated {EXPLORER_PATH.relative_to(ROOT).as_posix()} with {len(cases)} cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
