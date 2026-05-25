Param(
  [string]$RepoPath = ".",
  [string]$Exclude = "github_mcp.json",
  [string]$Message = ""
)

Set-Location $RepoPath
Write-Host "Repository path: $PWD"
git status --porcelain

# Stage all changes then unstage the sensitive file if present
git add -A
if (Test-Path $Exclude) {
  git reset -- $Exclude
}

if ([string]::IsNullOrWhiteSpace($Message)) {
  $dt = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
  $Message = "Agent commit: updates $dt"
}

git commit -m $Message
if ($LASTEXITCODE -ne 0) { Write-Host "Nothing to commit or commit failed (exit $LASTEXITCODE)" }

Write-Host "Pushing to remote..."
git push
if ($LASTEXITCODE -ne 0) { Write-Error "git push failed with exit code $LASTEXITCODE"; exit $LASTEXITCODE }

Write-Host "Done."
