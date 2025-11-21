import requests, json, pathlib
from datetime import datetime, timedelta

API_KEY = ## Add your Openweather API key
LAT = ## Add Latitude for weather
LON = ## Add Longitude for weather
UNITS = "metric"
URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNITS}"
AIR_POLLUTION = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
UNITS = "metric"

def main():
    response = requests.get(URL)
    air_response = requests.get(AIR_POLLUTION)
    air_data = air_response.json()
    air_number = air_data["list"][0]["main"]
    data = response.json()
    current = data.get("current", {})
    daily = data.get("daily", [])
    tz_offset = data.get("timezone_offset", 0)

    output = {
        "timezone": data.get("timezone"),
        "current": {
            "temp_c": current.get("temp"),
            "feels_like_c": current.get("feels_like"),
            "pressure": current.get("pressure"),
            "humidity": current.get("humidity"),
            "uvi": current.get("uvi"),
            "visibility": current.get("visibility"),
            "wind_speed": current.get("wind_speed"),
            "wind_deg": current.get("wind_deg"),
            "sunrise": unix_to_local_time(current.get("sunrise"), tz_offset),
            "sunset": unix_to_local_time(current.get("sunset"), tz_offset),
            "weather": current.get("weather", []),
            "air_quality": air_number.get("aqi"),
        },
        "daily": [
            {
            "day": datetime.utcfromtimestamp(day.get("dt") + tz_offset).strftime("%a"),
            "temp_min": day.get("temp", {}).get("min"),
            "temp_max": day.get("temp", {}).get("max"),
            "icon": day.get("weather", [{}])[0].get("icon"),
            "desc": day.get("weather", [{}])[0].get("description"),
            }
            for day in daily[:7]
        ],
    }
    data_dir = pathlib.Path("/home/pi/inky-weather/data")
    data_dir.mkdir(parents=True, exist_ok=True)
    with (data_dir / "weather.json").open("w") as f:
        json.dump(output, f, indent=2)

def unix_to_local_time(ts, offset_seconds):
    """Convert UNIX timestamp to HH:MM local time string."""
    if ts is None:
        return "--:--"
    dt = datetime.utcfromtimestamp(ts) + timedelta(seconds=offset_seconds)
    return dt.strftime("%-I:%M %p")

if __name__ == "__main__":

    main()
