#!/bin/bash
clear
echo "================================="
echo "       GAME LAUNCHER (LINUX)     "
echo "================================="
echo "[1] Play Python Game"
echo "[2] Play Go Game"
echo "================================="
read -p "Enter your choice (1 or 2): " choice

case $choice in
    1)
        echo "Launching Python Game..."
        # 'exec' replaces this bash process with Python entirely
        exec python3 ../python/implementation/starter.py
        ;;
    2)
        echo "Launching Go Game..."
        exec go run ../golang/guessing_1.go
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac
