@echo off
REM run this script to install dependencies from requirements.txt into your python virtual environment (venv).
REM NOTE: if you want to uninstall dependencies from your venv you must do it manually.
REM NOTE: recently added dependencies to requirements.txt not in your venv will be installed into your venv.

REM Check if a virtual environment is activated
if "%VIRTUAL_ENV%"=="" (
    echo No virtual environment is currently activated.
    exit /b 1
)

REM Get the path to the virtual environment
set "venv_path=%VIRTUAL_ENV%"

%venv_path%\Scripts\pip install -r ../requirements.txt