@echo off
REM Client Portfolio Dashboard Launcher for Windows

echo.
echo ========================================
echo  Client Portfolio Dashboard Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if requirements are installed
pip show streamlit >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages...
    pip install -r requirements.txt
    echo.
)

REM Run the dashboard
echo.
echo Starting Client Portfolio Dashboard...
echo Opening http://localhost:8501 in your browser...
echo.
echo Press Ctrl+C to stop the server
echo.
timeout /t 2 /nobreak

streamlit run app.py
