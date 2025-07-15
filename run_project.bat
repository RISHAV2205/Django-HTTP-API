@echo off
echo Activating virtual environment...
call env_1\Scripts\activate.bat

echo Starting Django server...
python manage.py runserver

pause
