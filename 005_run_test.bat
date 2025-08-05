@echo off
echo Testing Arithmetic Add (10 + 5)
curl -X POST http://localhost:5001/arithmetic/add ^
     -H "Content-Type: application/json" ^
     -d "{\"a\": 10, \"b\": 5}"
echo.

echo Testing Arithmetic Divide (20 / 4)
curl -X POST http://localhost:5001/arithmetic/div ^
     -H "Content-Type: application/json" ^
     -d "{\"a\": 20, \"b\": 4}"
echo.

echo Testing Scientific Log (x=2.718)
curl -X POST http://localhost:5002/scientific/log ^
     -H "Content-Type: application/json" ^
     -d "{\"x\": 2.718}"
echo.

echo Testing Scientific Square Root (x=16)
curl -X POST http://localhost:5002/scientific/sqrt ^
     -H "Content-Type: application/json" ^
     -d "{\"x\": 16}"
echo.

echo Testing Trigonometry Sin (angle=30)
curl -X POST http://localhost:5003/trigonometry/sin ^
     -H "Content-Type: application/json" ^
     -d "{\"angle\": 30}"
echo.

echo Testing Trigonometry Tan (angle=45)
curl -X POST http://localhost:5003/trigonometry/tan ^
     -H "Content-Type: application/json" ^
     -d "{\"angle\": 45}"
echo.

pause
