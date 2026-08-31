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
    parser.add_argument("--achievement", choices=sorted(ACHIEVEMENTS), required=True)
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit deterministic JSON instead of human-readable text.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
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
