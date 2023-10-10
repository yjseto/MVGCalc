@echo off

REM Check if a virtual environment is activated
if "%VIRTUAL_ENV%"=="" (
    echo No virtual environment is currently activated.
    exit /b 1
)

REM Get the path to the virtual environment
set "venv_path=%VIRTUAL_ENV%"

REM Prompt the user for confirmation
set /p "answer=Are you sure you want to delete all libraries in the virtual environment at %venv_path%? (y/n): "

if /i "%answer%"=="y" (
    REM List all installed packages and uninstall them one by one
    for /f %%i in ('pip freeze') do (
        pip uninstall -y %%i
    )

    REM REM Remove the virtual environment directory
    REM rmdir /s /q "%venv_path%"

    echo All libraries in the virtual environment have been deleted.
) else (
    echo Operation canceled.
)

