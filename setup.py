#!/usr/bin/env python3
"""
Client Portfolio Dashboard - Setup Script
Run this script to initialize the dashboard and install dependencies
"""

import os
import sys
import subprocess
from pathlib import Path

def create_directories():
    """Create required directories"""
    dirs = ['data', 'src', 'reports']
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✓ Directory '{dir_name}' ready")

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print(f"❌ Python 3.8+ required, but found {sys.version_info.major}.{sys.version_info.minor}")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_dependencies():
    """Install required packages"""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def verify_data_files():
    """Check if sample data files exist"""
    required_files = [
        'data/clients.csv',
        'data/engagements.csv',
        'data/deliverables.csv',
        'data/monthly_summaries.csv'
    ]
    
    print("\nVerifying data files...")
    missing = []
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✓ {file_path} found")
        else:
            print(f"⚠ {file_path} not found")
            missing.append(file_path)
    
    if missing:
        print(f"\n⚠ Missing {len(missing)} data file(s)")
        print("These files will be created when you first run the dashboard")
    
    return len(missing) == 0

def print_summary():
    """Print setup summary"""
    print("\n" + "="*50)
    print("✨ Setup Complete!")
    print("="*50)
    print("\nTo start the dashboard, run:")
    print("\n  streamlit run app.py\n")
    print("The dashboard will open in your browser at:")
    print("  http://localhost:8501")
    print("\nDocumentation: See README.md for detailed information")
    print("="*50 + "\n")

def main():
    """Run setup"""
    print("🚀 Client Portfolio Dashboard - Setup\n")
    print("="*50)
    
    check_python_version()
    create_directories()
    install_dependencies()
    verify_data_files()
    print_summary()

if __name__ == "__main__":
    main()
