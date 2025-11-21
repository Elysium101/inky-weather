#!/bin/bash
source /home/pi/.virtualenvs/pimoroni/bin/activate

python /home/pi/inky-weather/backend/fetch_weather.py

wkhtmltoimage \
  --width 800 \
  --height 480 \
  --crop-w 800 \
  --crop-h 480 \
  --javascript-delay 2000 \
  http://127.0.0.1:8000/web/ \
  /home/pi/inky-weather/data/screenshot.png

# 3. Process & display
python /home/pi/inky-weather/backend/show_screenshot.py
