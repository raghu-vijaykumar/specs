#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT_DIR"

STAGED_FILES="$(git diff --cached --name-only --diff-filter=ACMR)"

if [ -z "$STAGED_FILES" ]; then
  exit 0
fi

CODE_FILES="$(printf '%s
' "$STAGED_FILES" | grep -E '\.(ts|tsx|js|jsx|py|go|rb|java|cs|php|swift|kt|rs|c|cpp|h|hpp)$' || true)"

if [ -z "$CODE_FILES" ]; then
  exit 0
fi

echo "Commit gate reminder:"
echo "- If this change touches architecture-sensitive code, run improve-codebase-architecture before finishing."
echo "- If this changes behavior or interfaces, run code-review-and-quality or code-review before merging."
echo "- For framework-specific implementation, pair source-driven-development with opensrc when internals matter."
