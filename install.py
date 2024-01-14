#!/usr/bin/env python3

import os
import subprocess
import platform

def install_dependencies():
    try:
        print("🚀 Installing dependencies...")
        subprocess.run([get_pip_command(), 'install', '--upgrade', 'requests', 'beautifulsoup4', 'tqdm', 'tabulate'], check=True)
        print("✅ Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")

def run_lumina_proxy_script():
    try:
        print("🔄 Running LuminaProxy script...")
        subprocess.run([get_python_command(), 'lumina.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running LuminaProxy script: {e}")

def get_pip_command():
    if platform.system().lower() == 'windows':
        return 'pip'
    else:
        return 'pip3'

def get_python_command():
    if platform.system().lower() == 'windows':
        return 'python'
    else:
        return 'python3'

def main():
    print("🌟 Welcome to LuminaProxy Installer 🌟")

    # Check if running as root (sudo)
    if os.geteuid() == 0:
        print("❌ Please run this script without sudo or as root. LuminaProxy should not require elevated permissions.")
        return

    install_dependencies()
    run_lumina_proxy_script()

if __name__ == "__main__":
    main()
      
