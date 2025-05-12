@echo off
REM Get the folder where this .bat file lives
set SCRIPT_DIR=%~dp0
REM Remove trailing backslash
set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

REM Launch Windows Terminal in that folder and run the program
wt.exe -d "%SCRIPT_DIR%" cmd /k "g++ project8_converter.cpp -o project8_converter.exe && project8_converter.exe && pause"
