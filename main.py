#!/usr/bin/env python3
"""Write the plan text to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no randomness,
no clock, no environment input. Creates /output only when it is missing
(the grader mounts it); never deletes it. The plan itself is a fixed
string constant, so the output cannot drift between runs.
"""

import os

PLAN = (
    "Day 1: find 30 local businesses with slow sites via Google Maps, "
    "audit each free with PageSpeed, email the owner a 1-page fix list. "
    "Sell the $49 fix, built by code overnight. "
    "10 sales = $490 in 30 days. "
    "Edge: the free audit opens doors cold pitches can't; outreach runs 24/7."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
