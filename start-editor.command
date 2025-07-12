#!/bin/bash
# Albania Travel Metadata Editor - macOS Launcher
# Double-click this file to start the JSON editor

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Change to that directory
cd "$DIR"

echo "🇦🇱 Albania Travel Metadata Editor"
echo "=================================="
echo "📍 Starting from: $DIR"
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found"
    python3 server.py
elif command -v python &> /dev/null; then
    echo "✅ Python found (checking version...)"
    python_version=$(python -c 'import sys; print(sys.version_info[0])')
    if [ "$python_version" = "3" ]; then
        python server.py
    else
        echo "❌ Python 2 detected, but Python 3 is required"
        echo "💡 Please install Python 3 or use 'python3' command"
        read -p "Press Enter to exit..."
        exit 1
    fi
else
    echo "❌ Python not found"
    echo "💡 Please install Python 3 from https://python.org"
    echo "📝 Or run manually with: python3 server.py"
    read -p "Press Enter to exit..."
    exit 1
fi

echo ""
echo "Press Enter to exit..."
read