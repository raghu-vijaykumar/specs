$ErrorActionPreference = 'Stop'

$root = git rev-parse --show-toplevel 2>$null
if (-not $root) {
  $root = (Get-Location).Path
}

Set-Location $root
$stagedFiles = git diff --cached --name-only --diff-filter=ACMR

if (-not $stagedFiles) {
  exit 0
}

$codeFiles = $stagedFiles | Where-Object { $_ -match '\.(ts|tsx|js|jsx|py|go|rb|java|cs|php|swift|kt|rs|c|cpp|h|hpp)$' }

if (-not $codeFiles) {
  exit 0
}

Write-Host 'Commit gate reminder:'
Write-Host '- If this change touches architecture-sensitive code, run improve-codebase-architecture before finishing.'
Write-Host '- If this changes behavior or interfaces, run code-review-and-quality or code-review before merging.'
Write-Host '- For framework-specific implementation, pair source-driven-development with opensrc when internals matter.'
