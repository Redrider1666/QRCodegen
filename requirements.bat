@echo off

echo Installing librarys...
echo.

pip install pillow qrcode

if %errorlevel% neq 0 (
    echo Error to install the requirements.
    echo Verify if you have python installed in your computer.
    pause
    exit /b
)

echo All libraries installed successfully.
echo.

echo Starting the program...
echo.

python app.py

pause
