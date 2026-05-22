import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    humidity = current["humidity"]
    weather = current["weatherDesc"][0]["value"]

    print("\nWeather Information")
    print("-------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}%")

except Exception as e:
    print("Error:", e)