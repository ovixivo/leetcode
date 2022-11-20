@echo off
set /p "folderName=Enter Question Title: "
set /p "choice=Question Type: 1 - Python | 2 - SQL  "
mkdir "%folderName%"
cd "%folderName%"
if %choice%==1 (break>"solution.py")
if %choice%==2 (break>"solution.sql")

break>"question.md"
