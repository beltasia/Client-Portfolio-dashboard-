#!/bin/bash

# Client Portfolio Dashboard Launcher for macOS/Linux

echo ""
echo "========================================"
echo "  Client Portfolio Dashboard Launcher"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from python.org or using your package manager"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
source venv/bin/activate

# Check if requirements are installed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "Installing required packages..."
    pip install -r requirements.txt
    echo ""
fi

# Run the dashboard
echo ""
echo "Starting Client Portfolio Dashboard..."
echo "Opening http://localhost:8501 in your browser..."
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
sleep 2

streamlit run app.py
