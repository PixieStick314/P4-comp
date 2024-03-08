@echo off
setlocal

REM Set the path to the ANTLR4 jar file
set ANTLR_JAR_PATH=antlr-4.13.1-complete.jar

REM The root directory of the project, assuming this script runs from the project root
set PROJECT_ROOT=%CD%

REM The directory where your ANTLR grammar file is located
set GRAMMAR_DIR=%PROJECT_ROOT%\src\grammar_files

REM The directory where you want the generated files to go
set OUTPUT_DIR=%GRAMMAR_DIR%\generated

REM Check if the output directory exists, if not, create it
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

REM Prompt for the grammar file name without extension
set /p GrammarName="Enter the grammar file name: "
set GrammarFile=%GrammarName%

REM Generate the parser, lexer, and other related files using ANTLR
echo Generating ANTLR files for %GrammarFile%...
java -jar "%ANTLR_JAR_PATH%" -Dlanguage=Python3 -o "%OUTPUT_DIR%" "%GRAMMAR_DIR%\%GrammarFile%" -visitor -no-listener

echo Generation complete.
pause
endlocal