@echo off
REM Script para inicializar repositório Git e fazer primeiro push

SET REPO_NAME=NyraPilot
SET GITHUB_URL=https://github.com/Andynee504/NyraPilot

cd /d %~dp0

git init
git add .
git commit -m "Versão inicial do NyraPilot"
git branch -M main
git remote add origin %GITHUB_URL%
git push -u origin main

pause
