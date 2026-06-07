<#
.SYNOPSIS
    Audit implementation specs to ensure they contain a Testing & Validation section.
.DESCRIPTION
    Checks all spec.md files under specs/general/ (excluding concept/reference
    specs) for a "## Testing & Validation" heading. Concept specs (themes,
    typography, icons, architecture, doc-sync, legal, system) and all mobile
    UI component specs are excluded — they describe visual/interaction
    patterns, not buildable code.
    Exit code 0 = all pass.
.EXAMPLE
    powershell -File audit.ps1
#>

# Directories that are concept/reference, not implementation
$exclude = @(
    "architecture", "doc-sync", "legal", "system",
    "themes", "typography", "icons"
)

$missing = @()
$specs = Get-ChildItem -LiteralPath "specs" -Recurse -Filter "spec.md"

foreach ($spec in $specs) {
    $parentDir = $spec.Directory.Name
    if ($parentDir -in $exclude) { continue }
    # Also skip all mobile specs (UI component descriptions)
    if ($spec.FullName -match "\\specs\\mobile\\") { continue }

    $content = Get-Content -LiteralPath $spec.FullName -Raw -ErrorAction SilentlyContinue
    if ($content -notmatch "Testing & Validation") {
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
