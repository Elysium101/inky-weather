import subprocess
import time
import os
import sys

BASE = "/home/pi/inky-weather"

# 1. Fetch latest weather
subprocess.run(
    [sys.executable, f"{BASE}/backend/fetch_weather.py"], check=True
)

# 2. Start a temporary HTTP server
server = subprocess.Popen(
    [sys.executable, "-m", "http.server", "8000"],
    cwd=BASE,
)

# Give it time to start
time.sleep(2)

# 3. Render HTML to screenshot
subprocess.run([
    "wkhtmltoimage",
    "--width", "800",
    "--height", "480",
    "--crop-w", "800",
    "--crop-h", "480",
    "--javascript-delay", "2000",
    "http://127.0.0.1:8000/web/",
    f"{BASE}/data/screenshot.png",
], check=True)

# 4. Kill the server
server.terminate()
server.wait()

# 5. Display
subprocess.run(
    [sys.executable, f"{BASE}/backend/show_screenshot.py"], check=True
)
