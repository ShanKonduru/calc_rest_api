@echo off
echo ================================
echo Testing Arithmetic API (Basic Auth)
echo ================================

REM Test Add
curl -X POST http://localhost:5001/arithmetic/add ^
     -u admin:secret123 ^
     -H "Content-Type: application/json" ^
     -d "{\"a\": 10, \"b\": 5}"
echo.

REM Test Subtract
curl -X POST http://localhost:5001/arithmetic/sub ^
     -u admin:secret123 ^
     -H "Content-Type: application/json" ^
     -d "{\"a\": 20, \"b\": 7}"
echo.

REM Test Multiply
curl -X POST http://localhost:5001/arithmetic/mul ^
     -u admin:secret123 ^
     -H "Content-Type: application/json" ^
     -d "{\"a\": 3, \"b\": 4}"
echo.

REM Test Divide
curl -X POST http://localhost:5001/arithmetic/div ^
     -u admin:secret123 ^
     -H "Content-Type: application/json" ^
     -d "{\"a\": 100, \"b\": 25}"
echo.

echo ================================
echo Testing Scientific API (API Key)
echo ================================

REM Test Power
curl -X POST http://localhost:5002/scientific/power ^
     -H "x-api-key: token_string" ^
     -H "Content-Type: application/json" ^
     -d "{\"base\": 2, \"exp\": 3}"
echo.

REM Test Square Root
curl -X POST http://localhost:5002/scientific/sqrt ^
     -H "x-api-key: token_string" ^
     -H "Content-Type: application/json" ^
     -d "{\"x\": 16}"
echo.

REM Test Logarithm
curl -X POST http://localhost:5002/scientific/log ^
     -H "x-api-key: token_string" ^
     -H "Content-Type: application/json" ^
     -d "{\"x\": 2.718}"
echo.

echo ==========================================
echo Testing Trigonometric API (Basic Auth + API Key)
echo ==========================================

REM Test Sin
curl -X POST http://localhost:5003/trigonometry/sin ^
     -u admin:secret123 ^
     -H "x-api-key: token_string" ^
     -H "Content-Type: application/json" ^
     -d "{\"angle\": 30}"
echo.

REM Test Cos
curl -X POST http://localhost:5003/trigonometry/cos ^
     -u admin:secret123 ^
     -H "x-api-key: token_string" ^
     -H "Content-Type: application/json" ^
     -d "{\"angle\": 60}"
echo.

REM Test Tan
curl -X POST http://localhost:5003/trigonometry/tan ^
     -u admin:secret123 ^
     -H "x-api-key: token_string" ^
     -H "Content-Type: application/json" ^
     -d "{\"angle\": 45}"
echo.

echo All API tests completed.
pause
