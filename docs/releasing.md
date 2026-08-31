# Release Process

The project uses semantic versioning conventions and keeps user-visible changes in `CHANGELOG.md`.

## Versioning

- **Patch** (`0.1.0` → `0.1.1`): bug fixes and documentation corrections that do not change the public interface.
- **Minor** (`0.1.0` → `0.2.0`): backward-compatible features such as a new CLI output mode.
- **Major** (`0.x`/`1.x` → next major): incompatible public-interface changes once the project has a stable 1.0 contract.

## Release checklist

1. Confirm `main` is green in all required workflows.
2. Review open issues and decide what belongs in the release.
3. Update the `Unreleased` section in `CHANGELOG.md` and move completed work under the new version.
4. Update the version in `pyproject.toml`.
5. Run the full unit-test suite locally or through CI.
6. Open a focused release pull request.
7. Merge only after checks pass.
8. Create a Git tag using the form `vX.Y.Z`.
9. Create a GitHub release whose notes summarize the matching changelog entry.
10. Verify the release points at the expected commit and contains no secrets or generated junk.

## Release quality bar

A release should represent a coherent project milestone. Tags and releases should not be created solely to inflate repository activity.
