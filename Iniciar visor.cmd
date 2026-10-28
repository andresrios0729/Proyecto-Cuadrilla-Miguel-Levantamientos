@echo off
cd /d "%~dp0"
"C:\Users\riost\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" iniciar.py
if errorlevel 1 pause
