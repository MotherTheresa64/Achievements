"""Command-line interface for Achievement Lab."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from importlib.metadata import PackageNotFoundError, version

from .progress import ACHIEVEMENTS, get_progress


def package_version() -> str:
    """Return the installed package version, with a source-tree fallback."""
    try:
        return version("achievement-lab")
    except PackageNotFoundError:
        return "0+unknown"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report progress toward a GitHub achievement tier.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {package_version()}")
    parser.add_argument(
        "--list",
        action="store_true",
        dest="list_achievements",
        help="List supported achievements and their tracked thresholds.",
    )
    parser.add_argument("--achievement", choices=sorted(ACHIEVEMENTS))
    parser.add_argument("--count", type=int)
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit deterministic JSON instead of human-readable text.",
    )
    return parser


def print_catalog() -> None:
    """Print the supported achievement catalog in a stable order."""
    for achievement in sorted(ACHIEVEMENTS):
        thresholds = ", ".join(str(value) for value in ACHIEVEMENTS[achievement])
        print(f"{achievement}: {thresholds}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_achievements:
        print_catalog()
        return

    if args.achievement is None or args.count is None:
        parser.error("--achievement and --count are required unless --list is used")

    progress = get_progress(args.achievement, args.count)

    if args.as_json:
        print(json.dumps(asdict(progress), sort_keys=True))
        return

    display_name = args.achievement.replace("-", " ").title()
    print(f"{display_name}: {progress.count}")
    if progress.next_tier is None:
        print("Highest tracked tier reached")
        return

    print(f"Next tier: {progress.next_tier} at {progress.next_threshold}")
    print(f"Remaining: {progress.remaining}")


if __name__ == "__main__":
    main()
