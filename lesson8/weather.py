import requests
import datetime
import json
import os

CACHE_FILE = "weather_cache.json"
DEFAULT_LATITUDE = 51.1079    #  Wrocław, Poland., this is just assumption but not really values.
DEFAULT_LONGITUDE = 17.0385   # Wrocław, Poland

def get_next_day():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)

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
        print("API error:", e)
        return None

def get_location():
    lat_input = input(f"Enter latitude (default {DEFAULT_LATITUDE} for Wrocław): ").strip()
    lon_input = input(f"Enter longitude (default {DEFAULT_LONGITUDE} for Wrocław): ").strip()
    try:
        lat = float(lat_input) if lat_input else DEFAULT_LATITUDE
        lon = float(lon_input) if lon_input else DEFAULT_LONGITUDE
        return lat, lon
    except ValueError:
        print("Invalid latitude or longitude. Using default Wrocław coordinates.")
        return DEFAULT_LATITUDE, DEFAULT_LONGITUDE

def main():
    date_input = input("Enter date (YYYY-mm-dd) or press Enter for next day: ").strip()
    if date_input == "":
        date = get_next_day()
    elif validate_date(date_input):
        date = date_input
    else:
        print("Invalid date format.")
        return

    latitude, longitude = get_location()

    cache = load_cache()
    cache_key = f"{date}{latitude}{longitude}"
    if cache_key in cache:
        precip = cache[cache_key]
        print(f"Result loaded from cache for {date} at ({latitude}, {longitude}).")
    else:
        precip = fetch_precipitation(date, latitude, longitude)
        cache[cache_key] = precip
        save_cache(cache)

    if precip is None or precip < 0:
        print("I don't know")
    elif precip == 0.0:
        print("It will not rain")
    elif precip > 0.0:
        print(f"It will rain (precipitation: {precip} mm)")
    else:
        print("I don't know")

if __name__ == "__main__":
    main()