# GitHub Achievements Lab

A public workflow lab for practicing real GitHub engineering habits: branching, pull requests, issue tracking, automated testing, repository policy, and CI.

> Profile achievements are a fun side effect. The repository is intentionally transparent about its purpose and does not present lab activity as outside collaboration or production experience.

## Purpose

This repository combines a small, testable Python utility with a GitHub-native development workflow. It provides a safe place to exercise collaboration and automation features end-to-end while leaving behind code and process that can actually be inspected.

## Achievement progress utility

The included Python package reports progress toward community-observed tiers for several GitHub profile achievements.

```bash
python -m pip install -e .
python -m achievement_lab --achievement pull-shark --count 7
```

Example:

```text
Pull Shark: 7
Next tier: bronze at 16
Remaining: 9
```

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

### Tracked tier thresholds

| Achievement | Base | Bronze | Silver | Gold |
| --- | ---: | ---: | ---: | ---: |
| Pull Shark | 2 | 16 | 128 | 1024 |
| Pair Extraordinaire | 1 | 10 | 24 | 48 |
| Galaxy Brain | 2 | 8 | 16 | 32 |
| Starstruck | 16 | 128 | 512 | 4096 |

These thresholds are community-observed rather than a stable public API contract. GitHub currently describes Achievements as a public-preview feature and does not publish a complete unlock table, so values are isolated in the code and can be updated if behavior changes.

## What this repo demonstrates

- Issue-driven development
- Feature branches and pull requests
- Scoped, conventional-style commit messages
- Typed Python and a CLI entry point
- Unit testing
- Multi-version GitHub Actions CI
- Repository validation automation
- Pull-request and issue templates
- CODEOWNERS metadata
- Contribution and security policies
- Python packaging through `pyproject.toml`

## Workflow

1. Open or select an issue.
2. Create a focused branch.
3. Make a small, testable change.
4. Open a pull request describing the change.
5. Verify automated checks.
6. Merge and close the related work.

## Why this exists

Hiring credibility comes from inspectable work more than from badge count alone. This repository therefore uses achievement-oriented practice as a reason to demonstrate the same repository maintenance, automation, testing, and review workflow used on larger projects.

## License

MIT. See `LICENSE`.
