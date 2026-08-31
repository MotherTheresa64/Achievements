# Achievements

A small, testable GitHub workflow lab built to demonstrate real repository-maintenance habits: issue-driven work, feature branches, pull requests, automated testing, CI, documentation, and release discipline.

> The point of this repository is not empty activity. Every change should leave behind something reviewable: code, tests, documentation, automation, or project process.

## What it does

The included Python utility models several GitHub profile achievement milestones and reports progress toward the next tier. It intentionally uses only the Python standard library so the core logic is easy to inspect and test.

## Engineering practices demonstrated

- issue-driven development
- conventional-style commit messages
- short-lived feature branches
- pull-request based changes
- automated unit tests
- GitHub Actions continuous integration
- typed Python code
- project metadata through `pyproject.toml`
- contribution, security, and conduct policies
- issue and pull-request templates
- changelog-driven releases

## Quick start

```bash
python -m achievement_lab --achievement pull-shark --count 7
```

Example output:

```text
Pull Shark: 7
Next tier: bronze at 16
Remaining: 9
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Supported milestones

| Achievement | Base | Bronze | Silver | Gold |
| --- | ---: | ---: | ---: | ---: |
| Pull Shark | 2 | 16 | 128 | 1024 |
| Pair Extraordinaire | 1 | 10 | 24 | 48 |
| Galaxy Brain | 2 | 8 | 16 | 32 |
| Starstruck | 16 | 128 | 512 | 4096 |

Non-tiered achievements can be documented separately because they do not fit the same progression model.

## Repository roadmap

- [x] Core progress model
- [x] CLI interface
- [x] Unit-test suite
- [x] CI workflow
- [ ] Repository policy and contribution templates
- [ ] Changelog and first tagged release
- [ ] Additional achievement metadata and links to official documentation

## Why this repository exists

GitHub achievements are fun profile markers, but hiring credibility comes more from the work behind them. This repository therefore doubles as a compact example of maintainable engineering workflow rather than a collection of meaningless commits.

## License

MIT. See `LICENSE`.
