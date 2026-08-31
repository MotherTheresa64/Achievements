import unittest

from achievement_lab.progress import get_progress


class ProgressTests(unittest.TestCase):
    def test_reports_remaining_before_base_tier(self) -> None:
        progress = get_progress("pull-shark", 1)
        self.assertIsNone(progress.current_tier)
        self.assertEqual(progress.next_tier, "base")
        self.assertEqual(progress.remaining, 1)

    def test_reports_next_tier_after_base(self) -> None:
        progress = get_progress("pull-shark", 7)
        self.assertEqual(progress.current_tier, "base")
        self.assertEqual(progress.next_tier, "bronze")
        self.assertEqual(progress.next_threshold, 16)
        self.assertEqual(progress.remaining, 9)

    def test_reports_completion_at_highest_tier(self) -> None:
        progress = get_progress("galaxy-brain", 40)
        self.assertEqual(progress.current_tier, "gold")
        self.assertIsNone(progress.next_tier)
        self.assertEqual(progress.remaining, 0)

    def test_rejects_negative_counts(self) -> None:
        with self.assertRaises(ValueError):
            get_progress("starstruck", -1)

    def test_unknown_achievement_raises_key_error(self) -> None:
        with self.assertRaises(KeyError):
            get_progress("unknown", 1)


if __name__ == "__main__":
    unittest.main()
