#!/usr/bin/env python3
"""Put one short plan for turning $100 into more money in /output/entry.txt.

The text never changes, so each run writes the same bytes — run it twice and the file comes out identical.
It uses only the standard library, reaches no network,
reads no clock and no environment, and rolls no dice.
The output folder is made only when it is absent; nothing is removed.
"""

import os

PLAN = (
    "Day 1: search Google Maps for 30 shops with slow sites, "
    "run a PageSpeed check on each, and mail the owner a repair list. "
    "Charge $49 for the fix, coded overnight. "
    "Ten sales is $490 in 30 days, $100 untouched. "
    "Free checks open doors cold pitches can't; outreach runs 24/7."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(PLAN)


if __name__ == "__main__":
    main()
