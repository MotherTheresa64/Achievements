# GitHub Achievements Lab

A public workflow lab for practicing real GitHub engineering habits: issue-driven development, branching, pull requests, automation, testing, release hygiene, and repository maintenance.

## Purpose

This repository exists to exercise GitHub workflows end-to-end while keeping the work transparent and technically useful. Profile achievements may result from the activity, but the repository is intentionally structured around real code, tests, documentation, automation, and project-maintenance practices.

## What it does

The repository includes a small typed Python utility that models several GitHub profile-achievement milestones and reports progress toward the next tier. The implementation intentionally uses only the Python standard library so the core logic stays easy to inspect and test.

For eligibility notes, evidence quality, unavailable badges, and collaboration requirements, see [`docs/achievements.md`](docs/achievements.md). Release history lives in [`CHANGELOG.md`](CHANGELOG.md), with the release checklist in [`docs/releasing.md`](docs/releasing.md).

## Engineering practices demonstrated

- issue-driven development
- short-lived feature branches
- pull-request based changes
- conventional-style commit messages
- typed Python code
- automated unit tests
- GitHub Actions continuous integration
- project metadata through `pyproject.toml`
- contribution, security, and ownership policies
- issue and pull-request templates
- repository structure validation
- changelog-driven releases

## Quick start

```bash
python -m pip install -e .
python -m achievement_lab --achievement pull-shark --count 7
```

Example output:

```text
Pull Shark: 7
Next tier: bronze at 16
Remaining: 9
```

For machine-readable output, add `--json`:

```bash
python -m achievement_lab --achievement pull-shark --count 7 --json
```

```json
{"achievement": "pull-shark", "count": 7, "current_tier": "base", "next_threshold": 16, "next_tier": "bronze", "remaining": 9}
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Supported milestone data

| Achievement | Base | Bronze | Silver | Gold |
| --- | ---: | ---: | ---: | ---: |
| Pull Shark | 2 | 16 | 128 | 1024 |
| Pair Extraordinaire | 1 | 10 | 24 | 48 |
| Galaxy Brain | 2 | 8 | 16 | 32 |
| Starstruck | 16 | 128 | 512 | 4096 |

## Workflow

1. Open or select an issue.
2. Create a focused branch.
3. Make a testable change.
4. Open a pull request describing the change.
5. Verify automated checks.
6. Merge and close the related work.

## Roadmap

- [x] Repository purpose and contribution workflow
- [x] Collaboration templates and security policy
- [x] Repository structure validation
- [x] Core progress model
- [x] CLI interface
- [x] Unit-test suite
- [x] Multi-version Python CI
- [x] Achievement metadata and evidence reference
- [x] Changelog and release process
- [ ] First tagged GitHub release

## Intent

GitHub achievements are a fun side effect, but this repository is maintained as an inspectable engineering exercise rather than as fake outside collaboration or production experience. Every change should leave behind useful code, tests, documentation, or process.

## License

MIT. See `LICENSE`.
