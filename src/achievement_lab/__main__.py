"""Command-line interface for Achievement Lab."""

from __future__ import annotations

import argparse

from .progress import ACHIEVEMENTS, get_progress


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report progress toward a GitHub achievement tier.")
    parser.add_argument("--achievement", choices=sorted(ACHIEVEMENTS), required=True)
    parser.add_argument("--count", type=int, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    progress = get_progress(args.achievement, args.count)
    display_name = args.achievement.replace("-", " ").title()

    print(f"{display_name}: {progress.count}")
    if progress.next_tier is None:
        print("Highest tracked tier reached")
        return

    print(f"Next tier: {progress.next_tier} at {progress.next_threshold}")
    print(f"Remaining: {progress.remaining}")


if __name__ == "__main__":
    main()
