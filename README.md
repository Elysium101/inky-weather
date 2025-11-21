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

## 🌤️ How It Works

1. `fetch_weather.py` fetches updated weather via OpenWeather API.  
2. A temporary HTTP server serves the `web/` folder.  
3. `wkhtmltoimage` renders the dashboard at 1600×960.  
4. `show_screenshot.py` downscales, sharpens, applies palette, and displays the image.  
5. A cron job runs this process every 3 hours.



📸 Screenshots

![PXL_20251121_113543922](https://github.com/user-attachments/assets/0e50b0f9-d225-466a-9b87-40d20ea4b7c9)


## 🛠️ Project Structure
```bash
inky-weather/
│
├── backend/
│   ├── fetch_weather.py      # Fetches weather + outputs JSON
│   ├── main.py               # (Optional) service runner
│   ├── run_pipeline.py       # Full automated pipeline
│   ├── show_screenshot.py    # High-quality Inky renderer
│
├── web/
│   ├── index.html            # Frontend dashboard
│   ├── js/app.js             # Dynamic weather logic
│   ├── css/style.css         # Dashboard styling
│   └── assets/icons/         # Weather icons
│
├── data/
│   ├── weather.json          # Latest fetched weather
│   └── screenshot.png        # Rendered dashboard image
│
└── README.md
