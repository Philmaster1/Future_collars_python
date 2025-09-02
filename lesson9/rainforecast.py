import requests
import datetime
import json
import os

# 🌍 Default location: Wrocław, Poland
CACHE_FILE = "weather_cache.json"
DEFAULT_LATITUDE = 51.1079
DEFAULT_LONGITUDE = 17.0385

class WeatherForecast:
    def _init_(self, cache_file=CACHE_FILE):
        self.cache_file = cache_file
        self._cache = self._load_cache()

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "r") as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        with open(self.cache_file, "w") as f:
            json.dump(self._cache, f)

    def _setitem_(self, key, value):
        self._cache[key] = value
        self._save_cache()

    def _getitem_(self, key):
        return self._cache.get(key, None)

    def _iter_(self):
        return iter(self._cache)

    def items(self):
        for date, weather in self._cache.items():
            yield (date, weather)

def get_next_day():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def fetch_precipitation(date, latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&daily=precipitation_sum"
        f"&timezone=Europe%2FLondon&start_date={date}&end_date={date}"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        precip = data.get("daily", {}).get("precipitation_sum", [None])[0]
        return precip
    except Exception as e:
        print("🌐 API error:", e)
        return None

def get_location():
    lat_input = input(f"📍 Enter latitude (default {DEFAULT_LATITUDE} for Wrocław): ").strip()
    lon_input = input(f"📍 Enter longitude (default {DEFAULT_LONGITUDE} for Wrocław): ").strip()
    try:
        lat = float(lat_input) if lat_input else DEFAULT_LATITUDE
        lon = float(lon_input) if lon_input else DEFAULT_LONGITUDE
        return lat, lon
    except ValueError:
        print("⚠️ Invalid latitude or longitude. Using default Wrocław coordinates.")
        return DEFAULT_LATITUDE, DEFAULT_LONGITUDE

def main():
    weather_forecast = WeatherForecast()
    date_input = input("📅 Enter date (YYYY-mm-dd) or press Enter for next day: ").strip()
    if date_input == "":
        date = get_next_day()
    elif validate_date(date_input):
        date = date_input
    else:
        print("❌ Invalid date format.")
        return

    latitude, longitude = get_location()
    cache_key = f"{date}{latitude}{longitude}"

    precip = weather_forecast[cache_key]
    if precip is not None:
        print(f"✅ Result loaded from cache for {date} at ({latitude}, {longitude}).")
    else:
        precip = fetch_precipitation(date, latitude, longitude)
        weather_forecast[cache_key] = precip

    # 🌦️ Forecast interpretation
    if precip is None or precip < 0:
        print("🤷 I don't know")
    elif precip == 0.0:
        print("☀️ It will not rain")
    elif precip > 0.0:
        print(f"🌧️ It will rain (precipitation: {precip} mm)")
    else:
        print("🤷 I don't know")

    # 🗂️ Display cached forecasts
    print("\n📁 Saved forecasts:")
    for key in weather_forecast:
        print(f"{key}: {weather_forecast[key]}")
    print("\n📋 Forecast items:")
    for date, weather in weather_forecast.items():
        print(f"{date}: {weather}")

if __name__ == "__main__":
        main()