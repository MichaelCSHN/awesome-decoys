#!/usr/bin/env python3
"""Repository integrity checks for awesome-decoys."""

from __future__ import annotations

import csv
import json
import pathlib
import re
import sys
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parents[1]


def read_csv(rel: str) -> list[dict[str, str]]:
    path = ROOT / rel
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def warn(warnings: list[str], message: str) -> None:
    warnings.append(message)


def check_unique(rows: list[dict[str, str]], key: str, rel: str, errors: list[str]) -> None:
    values = [row.get(key, "").strip() for row in rows]
    blanks = [idx + 2 for idx, value in enumerate(values) if not value]
    duplicates = [value for value, count in Counter(values).items() if value and count > 1]
    if blanks:
        fail(errors, f"{rel}: blank {key} at CSV lines {blanks}")
    if duplicates:
        fail(errors, f"{rel}: duplicate {key} values {duplicates}")


def check_case_sources(cases: list[dict[str, str]], sources: list[dict[str, str]], errors: list[str]) -> None:
    source_keys = {row["source_key"].strip() for row in sources}
    for row in cases:
        for key in [part.strip() for part in row.get("source_refs", "").split(";") if part.strip()]:
            if key not in source_keys:
                fail(errors, f"data/cases.csv: {row['case_id']} references missing source key {key}")


def check_source_quality_warnings(
    cases: list[dict[str, str]], sources: list[dict[str, str]], warnings: list[str]
) -> None:
    source_by_key = {row["source_key"].strip(): row for row in sources}
    for row in cases:
        refs = [part.strip() for part in row.get("source_refs", "").split(";") if part.strip()]
        if len(refs) < 2:
            warn(warnings, f"data/cases.csv: {row['case_id']} has fewer than 2 source_refs")
        tiers = [source_by_key.get(ref, {}).get("quality_tier", "").strip() for ref in refs]
        if refs and not any(tier.startswith("A") for tier in tiers):
            warn(warnings, f"data/cases.csv: {row['case_id']} has no A-tier source_refs")

    for row in sources:
        key = row.get("source_key", "").strip()
        if not row.get("url", "").strip():
            warn(warnings, f"data/sources.csv: {key} has a blank url")
        if row.get("notes", "").strip().upper().startswith("STUB:"):
            warn(warnings, f"data/sources.csv: {key} is still marked STUB")


def check_sources_markdown(sources: list[dict[str, str]], errors: list[str]) -> None:
    text = (ROOT / "references" / "sources.md").read_text(encoding="utf-8")
    md_keys = set(re.findall(r"^- `([^`]+)` -", text, flags=re.MULTILINE))
    csv_keys = {row["source_key"].strip() for row in sources}
    missing_in_csv = sorted(md_keys - csv_keys)
    if missing_in_csv:
        fail(errors, f"references/sources.md: keys missing from data/sources.csv: {missing_in_csv}")


def check_local_links(errors: list[str]) -> None:
    files = [
        *ROOT.glob("*.md"),
        *ROOT.glob("*.html"),
        *ROOT.glob("assets/*.html"),
        *ROOT.glob("assets/*.svg"),
        *ROOT.glob("docs/*.md"),
        *ROOT.glob("references/*.md"),
        *ROOT.glob("data/*.md"),
    ]
    link_re = re.compile(r"\[[^\]]+\]\(([^):#][^)]*)\)|(?:href|src)=\"([^\":#][^\"]*)\"")
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in link_re.finditer(text):
            target = (match.group(1) or match.group(2)).strip()
            if re.match(r"^(https?|mailto|data):", target) or target.startswith("#"):
                continue
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                rel = path.relative_to(ROOT).as_posix()
                fail(errors, f"{rel}: missing local link target {target}")


def check_case_explorer(cases: list[dict[str, str]], errors: list[str]) -> None:
    path = ROOT / "assets" / "cases-explorer.html"
    text = path.read_text(encoding="utf-8")
    match = re.search(r'const CASES = JSON\.parse\("(.*?)"\);', text, flags=re.DOTALL)
    if not match:
        fail(errors, "assets/cases-explorer.html: embedded CASES JSON not found")
        return
    embedded = json.loads(json.loads(f'"{match.group(1)}"'))
    csv_by_id = {row["case_id"]: row for row in cases}
    embedded_by_id = {row["case_id"]: row for row in embedded}
    if set(csv_by_id) != set(embedded_by_id):
        fail(errors, "assets/cases-explorer.html: embedded case IDs do not match data/cases.csv")
        return
    mismatches = []
    for case_id, row in csv_by_id.items():
        embedded_row = embedded_by_id[case_id]
        for field, value in row.items():
            if str(embedded_row.get(field, "")) != str(value):
                mismatches.append(case_id)
                break
    if mismatches:
        fail(errors, f"assets/cases-explorer.html: embedded cases differ from CSV: {mismatches[:20]}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    cases = read_csv("data/cases.csv")
    sources = read_csv("data/sources.csv")
    vendors = read_csv("data/vendors.csv")

    check_unique(cases, "case_id", "data/cases.csv", errors)
    check_unique(sources, "source_key", "data/sources.csv", errors)
    check_unique(vendors, "vendor_key", "data/vendors.csv", errors)
    check_case_sources(cases, sources, errors)
    check_source_quality_warnings(cases, sources, warnings)
    check_sources_markdown(sources, errors)
    check_local_links(errors)
    check_case_explorer(cases, errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    if warnings:
        print("Validation warnings:")
        for warning in warnings:
            print(f"- {warning}")

    print(
        "Validation passed: "
        f"{len(cases)} cases, {len(sources)} sources, {len(vendors)} vendors."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
