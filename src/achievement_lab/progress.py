"""Core achievement progress calculations.

Thresholds are community-observed and intentionally isolated in one mapping because
GitHub treats profile achievements as a preview feature and may change behavior.
"""

from __future__ import annotations

from dataclasses import dataclass


ACHIEVEMENTS: dict[str, tuple[int, ...]] = {
    "pull-shark": (2, 16, 128, 1024),
    "pair-extraordinaire": (1, 10, 24, 48),
    "galaxy-brain": (2, 8, 16, 32),
    "starstruck": (16, 128, 512, 4096),
}

TIER_NAMES = ("base", "bronze", "silver", "gold")


@dataclass(frozen=True, slots=True)
class Progress:
    achievement: str
    count: int
    current_tier: str | None
    next_tier: str | None
    next_threshold: int | None
    remaining: int


def get_progress(achievement: str, count: int) -> Progress:
    """Return progress for a supported tiered achievement.

    Raises:
        KeyError: If ``achievement`` is not supported.
        ValueError: If ``count`` is negative.
    """
    if count < 0:
        raise ValueError("count must be zero or greater")

    thresholds = ACHIEVEMENTS[achievement]
    earned_indexes = [index for index, threshold in enumerate(thresholds) if count >= threshold]
    current_index = earned_indexes[-1] if earned_indexes else None

    if current_index is None:
        next_index = 0
    elif current_index + 1 < len(thresholds):
        next_index = current_index + 1
    else:
        next_index = None

    current_tier = TIER_NAMES[current_index] if current_index is not None else None
    next_tier = TIER_NAMES[next_index] if next_index is not None else None
    next_threshold = thresholds[next_index] if next_index is not None else None
    remaining = max(0, next_threshold - count) if next_threshold is not None else 0

    return Progress(
        achievement=achievement,
        count=count,
        current_tier=current_tier,
        next_tier=next_tier,
        next_threshold=next_threshold,
        remaining=remaining,
    )
