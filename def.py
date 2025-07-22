def get_weather():
    city = input("Enter your city: ")
    print(f"Fetching weather for {city}...")

    # Mock weather data
    weather_data = {
        "Delhi": {"temp": "32°C", "condition": "Sunny"},
        "Mumbai": {"temp": "28°C", "condition": "Rainy"},
    }

    if city in weather_data:
        info = weather_data[city]
        print(f"Temperature: {info['temp']}, Condition: {info['condition']}")
    else:
        print("Sorry, no data available.")

get_weather()
