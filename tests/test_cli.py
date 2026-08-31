import io
import json
import unittest
from contextlib import redirect_stderr, redirect_stdout
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

    def test_catalog_output_is_sorted_and_complete(self) -> None:
        output = self.run_cli("--list").splitlines()
        self.assertEqual(
            output,
            [
                "galaxy-brain: 2, 8, 16, 32",
                "pair-extraordinaire: 1, 10, 24, 48",
                "pull-shark: 2, 16, 128, 1024",
                "starstruck: 16, 128, 512, 4096",
            ],
        )

    def test_missing_progress_arguments_are_rejected(self) -> None:
        errors = io.StringIO()
        with (
            patch("sys.argv", ["achievement_lab"]),
            redirect_stderr(errors),
            self.assertRaises(SystemExit) as exit_context,
        ):
            main()

        self.assertEqual(exit_context.exception.code, 2)
        self.assertIn("--achievement and --count are required", errors.getvalue())

    def test_version_flag(self) -> None:
        output = io.StringIO()
        with (
            patch("sys.argv", ["achievement_lab", "--version"]),
            patch("achievement_lab.__main__.package_version", return_value="0.1.0"),
            redirect_stdout(output),
            self.assertRaises(SystemExit) as exit_context,
        ):
            main()

        self.assertEqual(exit_context.exception.code, 0)
        self.assertIn("achievement_lab 0.1.0", output.getvalue())


if __name__ == "__main__":
    unittest.main()
