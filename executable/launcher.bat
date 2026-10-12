@echo off
cls
echo =================================
echo        GAME LAUNCHER (WINDOWS)   
echo =================================
echo [1] Play Python Game
echo [2] Play Go Game
echo =================================
set /p choice="Enter your choice (1 or 2): "

if "%choice%"=="1" (
    echo Launching Python Game...
    python ..\python\implementation\starter.py
    exit
) else if "%choice%"=="2" (
    echo Launching Go Game...
    go run ..\golang\guessing_1.go
    exit
) else (
    echo Invalid choice. Exiting.
    timeout /t 3 >nul
    exit /b 1
)

