# Day 43 – Dehradun Weather App (API error handling)

A command-line app that shows Dehradun's live weather using the free Open-Meteo API (no API key needed).

## Features
- Live temperature, humidity and wind speed
- No internet → friendly message instead of a crash
- Slow server → stops waiting after 10 seconds (timeout)
- Bad status code → shows the status instead of crashing

## How to run
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python weather_app.py`

## What I learned
- `try / except / else`: `else` runs only when no error happened
- `requests.exceptions.ConnectionError` (no internet) and `Timeout` (too slow)
- `timeout=10` so the app never waits forever
- Reading nested JSON: `data["current"]["temperature_2m"]`
- Test the error paths too – a typo in an `except` line only shows up when the error happens

## Planned upgrades
- Day 50: functions + temperature charts with Matplotlib
- Days 66–70: full weather dashboard – any city (geocoding API), friendly status messages, history