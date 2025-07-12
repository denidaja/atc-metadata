@echo off
REM Albania Travel Metadata Editor - Windows Launcher
REM Double-click this file to start the JSON editor

title Albania Travel Metadata Editor

echo 🇦🇱 Albania Travel Metadata Editor
echo ==================================
echo 📍 Starting from: %~dp0
echo.

REM Change to the script's directory
cd /d "%~dp0"

REM Check if Python 3 is available
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Python found
    python server.py
) else (
    py --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo ✅ Python found via py launcher
        py server.py
    ) else (
        echo ❌ Python not found
        echo 💡 Please install Python 3 from https://python.org
        echo 📝 Or run manually with: python server.py
        pause
        exit /b 1
    )
)

echo.
pause