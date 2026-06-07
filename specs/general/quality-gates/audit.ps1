<#
.SYNOPSIS
    Audit all spec files to ensure they contain a Testing & Validation section.
.DESCRIPTION
    Scans every spec.md under specs/ and reports any that lack a
    "## Testing & Validation" heading. Exit code 0 = all pass.
.EXAMPLE
    pwsh -File audit.ps1
#>

$missing = @()
$specs = Get-ChildItem -LiteralPath "specs" -Recurse -Filter "spec.md"

foreach ($spec in $specs) {
    $content = Get-Content -LiteralPath $spec.FullName -Raw -ErrorAction SilentlyContinue
    if ($content -notmatch "## Testing & Validation") {
        $missing += $spec.FullName.Replace("$PWD\", "")
    }
}

if ($missing.Count -eq 0) {
    Write-Host "PASS: All specs have a Testing & Validation section."
    exit 0
} else {
    Write-Host "FAIL: $($missing.Count) spec(s) missing Testing & Validation section:"
    $missing | ForEach-Object { Write-Host "  - $_" }
    exit 1
}
