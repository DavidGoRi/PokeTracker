# Sube los cambios de PokeTracker a GitHub (la web se actualiza sola en GitHub Pages).
# Uso: powershell -ExecutionPolicy Bypass -File subir.ps1 ["Mensaje del cambio"]
param([string]$Mensaje = "")

$ErrorActionPreference = 'Continue'
Set-Location -Path $PSScriptRoot

if (-not (Test-Path '.git')) {
    Write-Host 'Esta carpeta no es un repositorio de git.' -ForegroundColor Red
    exit 1
}

git add -A
$cambios = git status --porcelain
if (-not $cambios) {
    Write-Host 'No hay cambios que subir.' -ForegroundColor Yellow
    exit 0
}

if (-not $Mensaje) { $Mensaje = 'Actualizar PokeTracker ' + (Get-Date -Format 'yyyy-MM-dd HH:mm') }
git commit -m $Mensaje
if ($LASTEXITCODE -ne 0) { Write-Host 'Falló el commit.' -ForegroundColor Red; exit 1 }

# Trae antes los cambios hechos desde la web de GitHub (por ejemplo, editar el README)
git pull --rebase
if ($LASTEXITCODE -ne 0) {
    Write-Host 'Hay cambios en GitHub que chocan con los tuyos. Resuélvelos y vuelve a ejecutar el script.' -ForegroundColor Red
    exit 1
}

git push
if ($LASTEXITCODE -ne 0) { Write-Host 'Falló la subida (git push).' -ForegroundColor Red; exit 1 }

$usuario = gh api user --jq .login
Write-Host ''
Write-Host 'Subido. GitHub Pages tarda uno o dos minutos en actualizar la web:' -ForegroundColor Green
Write-Host "https://$($usuario.ToLower()).github.io/PokeTracker/"
