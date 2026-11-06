#!/usr/bin/env python3
"""Starter learning template: search the AI prompt-pattern library.

Usage:
    python3 scripts/pattern-search.py prompt-patterns-template.csv sop
    python3 scripts/pattern-search.py prompt-patterns-template.csv --category runbook
    python3 scripts/pattern-search.py prompt-patterns-template.csv --id P03

Searches the CSV by keyword (title, prompt, sample context) or filters by
category / id. Sample data only; no real company data.
"""
import argparse
import csv
import sys


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def show(row):
    print(f"[{row['id']}] {row['title']}  (category: {row['category']})")
    print(f"  Prompt: {row['prompt']}")
    print(f"  Sample context: {row['sample_context']}")
    print(f"  Check before publishing: {row['check_notes']}")
    print()


def main():
    ap = argparse.ArgumentParser(description="Search the prompt-pattern library.")
    ap.add_argument("csv_file", help="path to prompt-patterns-template.csv")
    ap.add_argument("keyword", nargs="?", help="keyword to search for")
    ap.add_argument("--category", help="filter by category (sop, runbook, ...)")
    ap.add_argument("--id", help="show one pattern by id (e.g. P03)")
    args = ap.parse_args()

    try:
        rows = load(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        sys.exit(1)

    if args.id:
        rows = [r for r in rows if r.get("id", "").lower() == args.id.lower()]
    if args.category:
        rows = [r for r in rows if r.get("category", "").lower() == args.category.lower()]
    if args.keyword:
        kw = args.keyword.lower()
        rows = [r for r in rows if kw in (r.get("title", "") + " " + r.get("prompt", "")
                                          + " " + r.get("sample_context", "")).lower()]

    if not rows:
        print("No matching patterns.")
        sys.exit(0)
    print(f"Patterns: {len(rows)}")
    print()
    for r in rows:
        show(r)


if __name__ == "__main__":
    main()
