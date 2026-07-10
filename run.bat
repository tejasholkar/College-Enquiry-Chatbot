@echo off
title CRCE Bot Chatbot
echo ========================================
echo     CRCE Bot - College Enquiry Chatbot
echo ========================================
echo.

echo [1/3] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo.
echo [2/3] Starting chatbot training...
python chatbot.py
if errorlevel 1 (
    echo WARNING: Chatbot initialization had issues, but continuing...
)

echo.
echo [3/3] Starting Flask server...
echo.
echo Server starting at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py

pause

