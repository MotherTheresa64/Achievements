#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "README.md"
  "CONTRIBUTING.md"
  ".github/PULL_REQUEST_TEMPLATE.md"
  ".github/ISSUE_TEMPLATE/documentation.yml"
)

for file in "${required_files[@]}"; do
  if [[ ! -s "$file" ]]; then
    echo "Required file is missing or empty: $file" >&2
    exit 1
  fi
done

grep -q "## Purpose" README.md
grep -q "## Transparency" CONTRIBUTING.md

echo "Repository structure checks passed."
