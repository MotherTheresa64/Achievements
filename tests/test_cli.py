import io
import json
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from achievement_lab.__main__ import main


class CliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> str:
        output = io.StringIO()
        with patch("sys.argv", ["achievement_lab", *args]), redirect_stdout(output):
            main()
        return output.getvalue()

    def test_human_readable_output(self) -> None:
        output = self.run_cli("--achievement", "pull-shark", "--count", "7")
        self.assertIn("Pull Shark: 7", output)
        self.assertIn("Next tier: bronze at 16", output)
        self.assertIn("Remaining: 9", output)

    def test_json_output(self) -> None:
        output = self.run_cli(
            "--achievement",
            "pair-extraordinaire",
            "--count",
            "10",
            "--json",
        )
        payload = json.loads(output)
        self.assertEqual(payload["achievement"], "pair-extraordinaire")
        self.assertEqual(payload["count"], 10)
        self.assertEqual(payload["current_tier"], "bronze")
        self.assertEqual(payload["next_tier"], "silver")
        self.assertEqual(payload["next_threshold"], 24)
        self.assertEqual(payload["remaining"], 14)

    def test_json_output_is_deterministic(self) -> None:
        first = self.run_cli("--achievement", "galaxy-brain", "--count", "3", "--json")
        second = self.run_cli("--achievement", "galaxy-brain", "--count", "3", "--json")
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
