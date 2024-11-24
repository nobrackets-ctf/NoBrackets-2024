cd "C:\Users\user\Desktop\finale_nbctf"

start /b python -m websockify 5901 127.0.0.1:5900 --web .\noVNC-master\

start /b python .\webapp\app.py

timeout /t 30

start /b python .\modbus_control.py