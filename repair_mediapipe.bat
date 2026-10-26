@echo off
cd /d "%~dp0"
call ".venv\Scripts\activate.bat"
python -m pip uninstall -y mediapipe
python -m pip install "numpy<2" "mediapipe==0.10.21" opencv-python pygame
python -c "from mediapipe.python.solutions import hands; print('MediaPipe OK')"
pause
