$ErrorActionPreference = "Stop"
$Installer = Join-Path $PSScriptRoot "scripts/install.py"
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $Installer
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python $Installer
} else {
    Write-Error "Python 3.9+ is required. Install it from python.org, then retry."
    exit 1
}
exit $LASTEXITCODE
