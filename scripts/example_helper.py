#!/usr/bin/env python3
"""Deterministic helper for the Communication Value Delivery skill.

This script provides two small utilities:
1. Estimate simple annual value from ROI assumptions.
2. Rank feedback items by adoption impact and effort.

It does not access the network, modify system files, or use external packages.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def _to_float(value: Any, default: float = 0.0) -> float:
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def estimate_roi(data: dict[str, Any]) -> dict[str, Any]:
    implementation_cost = _to_float(data.get("implementation_cost"))
    annual_operating_cost = _to_float(data.get("annual_operating_cost"))
    time_saved_minutes_per_use = _to_float(data.get("time_saved_minutes_per_use"))
    uses_per_month = _to_float(data.get("uses_per_month"))
    loaded_hourly_rate = _to_float(data.get("loaded_hourly_rate"))
    annual_revenue_enabled = _to_float(data.get("annual_revenue_enabled"))
    annual_risk_or_cost_avoided = _to_float(data.get("annual_risk_or_cost_avoided"))

    monthly_time_value = time_saved_minutes_per_use * uses_per_month * loaded_hourly_rate / 60
    annual_time_value = monthly_time_value * 12
    annual_gross_value = annual_time_value + annual_revenue_enabled + annual_risk_or_cost_avoided
    annual_net_value = annual_gross_value - annual_operating_cost
    monthly_gross_value = annual_gross_value / 12 if annual_gross_value else 0
    payback_months = implementation_cost / monthly_gross_value if monthly_gross_value else None

    return {
        "annual_time_value": round(annual_time_value, 2),
        "annual_gross_value": round(annual_gross_value, 2),
        "annual_net_value": round(annual_net_value, 2),
        "monthly_gross_value": round(monthly_gross_value, 2),
        "payback_months": round(payback_months, 2) if payback_months is not None else None,
        "note": "Estimate only. Validate assumptions before presenting as financial results.",
    }


def read_roi_csv(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            metric = (row.get("metric") or "").strip()
            if metric:
                data[metric] = row.get("value", "")
    return data


def rank_feedback(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    score_map = {"high": 3, "medium": 2, "low": 1}

    def score(item: dict[str, Any]) -> tuple[int, int, str]:
        impact = score_map.get(str(item.get("adoption_impact", "")).lower(), 0)
        effort = score_map.get(str(item.get("effort", "")).lower(), 0)
        # Higher impact first, lower effort second.
        return (-impact, effort, str(item.get("theme", "")))

    return sorted(items, key=score)


def main() -> int:
    parser = argparse.ArgumentParser(description="Support simple value delivery calculations.")
    sub = parser.add_subparsers(dest="command", required=True)

    roi = sub.add_parser("roi", help="Estimate ROI from a JSON or CSV assumptions file.")
    roi.add_argument("path", type=Path, help="Path to JSON or CSV assumptions file.")

    feedback = sub.add_parser("feedback", help="Rank feedback items from a JSON file.")
    feedback.add_argument("path", type=Path, help="Path to a JSON list of feedback items.")

    args = parser.parse_args()

    if args.command == "roi":
        if args.path.suffix.lower() == ".csv":
            data = read_roi_csv(args.path)
        else:
            data = json.loads(args.path.read_text(encoding="utf-8"))
        print(json.dumps(estimate_roi(data), indent=2))
        return 0

    if args.command == "feedback":
        items = json.loads(args.path.read_text(encoding="utf-8"))
        if not isinstance(items, list):
            raise ValueError("Feedback input must be a JSON list.")
        print(json.dumps(rank_feedback(items), indent=2))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
