def get_weather(city):
    # dummy response for now
    # later you can connect OpenWeather / GoMapsPro
    if not city:
        return {"error": "City is required"}

    return {
        "city": city,
        "temperature": "32°C",
        "condition": "Sunny",
        "humidity": "60%"
    }
