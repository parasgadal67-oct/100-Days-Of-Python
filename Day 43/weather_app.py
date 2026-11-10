import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=30.32&longitude=78.03&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.ConnectionError:
    print("No internet connection.Check your wi-fi.")
except requests.exceptions.Timeout:
    print("The server is too slow. Try again later.")
else:
    if response.status_code == 200:
        data = response.json()
        current = data["current"]
        print("====DEHRADUN WEATHER====")
        print("Temperature:", current["temperature_2m"],"°C")
        print("Humidity:", current["relative_humidity_2m"],"%")
        print("Wind speed:", current["wind_speed_10m"],"km/hr")
    else:
        print("Something went wrong. Status:", response.status_code)