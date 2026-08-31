# Security Policy

This repository is a public workflow lab and does not process production data or credentials.

## Reporting

If a change accidentally exposes a secret, credential, token, or sensitive value, do not copy it into a public issue. Revoke or rotate the affected credential first, then remove it from the repository history as appropriate.

## Repository rules

- Never commit API keys, passwords, access tokens, or private keys.
- Use repository or environment secrets for credentials required by automation.
- Keep GitHub Actions permissions scoped to the minimum required access.
- Treat third-party Actions and dependencies as supply-chain dependencies that require review.
