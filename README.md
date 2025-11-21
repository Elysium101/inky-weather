# 🖼️ Inky Weather Dashboard  
### Family Weather Dashboard for Raspberry Pi Zero W + Inky Impression 7.3"

This project creates a high-contrast, 7-day weather dashboard displayed on a **Pimoroni Inky Impression 7.3" e-paper display**, powered by a **Raspberry Pi Zero W**.

It fetches live weather data, renders a full HTML dashboard, screenshots it at high resolution, converts it to the Inky colour palette, and displays it automatically on a schedule.

---

## ✨ Features

- Full-screen HTML/CSS/JS weather dashboard  
- Dynamic current conditions (temperature, sunrise, sunset, humidity, wind, pressure, UV index, visibility, AQI)  
- Dynamic 7-day forecast with icons  
- High-resolution rendering pipeline  
  - Renders at 1600×960  
  - Downscales with LANCZOS  
  - Sharpens text  
  - Converts to official 7-colour Inky palette  
- Automatic updates (cron)  
- Runs completely offline after data fetch  
- Optimised for Raspberry Pi Zero W + Inky Impression 7.3"

---

## 🛠️ Project Structure

inky-weather/
│
├── backend/
│ ├── fetch_weather.py
│ ├── run_pipeline.py
│ ├── show_screenshot.py
│
├── web/
│ ├── index.html
│ ├── js/app.js
│ ├── css/style.css
│ └── assets/icons/
│
├── data/
│ ├── weather.json
│ └── screenshot.png
│
└── README.md


---

## 🌤️ How It Works

1. `fetch_weather.py` fetches updated weather via OpenWeather API.  
2. A temporary HTTP server serves the `web/` folder.  
3. `wkhtmltoimage` renders the dashboard at 1600×960.  
4. `show_screenshot.py` downscales, sharpens, applies palette, and displays the image.  
5. A cron job runs this process every 3 hours.



📸 Screenshots
Add photos here.

