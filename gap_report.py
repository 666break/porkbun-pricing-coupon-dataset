#!/usr/bin/env python3
"""Print Porkbun TLD rows sorted by first-year-to-renewal gap.

Reads porkbun-tld-prices-2026-11-22.csv from this script's directory unless
--csv is given. Uses only the Python standard library.
"""

import argparse
import csv
from pathlib import Path


def load_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser(
        description="Print Porkbun TLD rows sorted by first-year-to-renewal gap."
    )
    default_csv = Path(__file__).with_name("porkbun-tld-prices-2026-11-22.csv")
    parser.add_argument("--csv", default=str(default_csv), help="path to the price CSV")
    args = parser.parse_args()

    rows = load_rows(args.csv)
    rows.sort(key=lambda row: float(row["gap_usd"]), reverse=True)

    print(f"{'TLD':<8}{'First year':>12}{'Renewal':>12}{'Gap':>10}  Checked")
    for row in rows:
        first = float(row["first_year_usd"])
        renewal = float(row["renewal_usd"])
        gap = float(row["gap_usd"])
        print(
            f"{row['tld']:<8}${first:>11.2f}${renewal:>11.2f}${gap:>9.2f}"
            f"  {row['checked_date']}"
        )


if __name__ == "__main__":
    main()
