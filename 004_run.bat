@echo off
REM python src\\calc_app.py

@echo off
echo Starting Arithmetic API on port 5001...
start cmd /k "python src\arithmetic_app.py"

timeout /t 1 > nul

echo Starting Scientific API on port 5002...
start cmd /k "python src\scientific_app.py"

timeout /t 1 > nul

echo Starting Trigonometric API on port 5003...
start cmd /k "python src\trigonometry_app.py"

echo All servers launched in separate terminals.
pause
