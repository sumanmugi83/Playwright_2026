@echo off
echo Starting Gherkin to Playwright Converter...
echo Python Path: %LOCALAPPDATA%\Programs\Python\Python312\python.exe
echo App Path: %~dp0tools\app.py

"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" "%~dp0tools\app.py"

pause
