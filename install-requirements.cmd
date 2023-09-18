@echo off
REM run this script to install dependencies from requirements.txt into your python virtual environment (venv).
REM NOTE: if you want to uninstall dependencies from your venv you must do it manually.
REM NOTE: recently added dependencies to requirements.txt not in your venv will be installed into your venv.
.venv\Scripts\pip install -r requirements.txt