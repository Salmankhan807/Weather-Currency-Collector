import requests

class WeatherAPI:

     def get_weather(self, city):

        api_key = "ed17306a6a3e839d60320522ed2b4530"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        
        data = response.json()
        if data["cod"] != 200:
            print("City not found!")
            return
        weather_info = {
        "City": data["name"],
        "Temperature": f'{data["main"]["temp"]}°C',
        "Feels Like": f'{data["main"]["feels_like"]}°C',
        "Humidity": f'{data["main"]["humidity"]}%',
        "Wind Speed": f'{data["wind"]["speed"]} m/s',
        "Condition": data["weather"][0]["description"].title()
        }
        print("=" * 35)
        print("        WEATHER REPORT")
        print("=" * 35)

        for key, value in weather_info.items():
            print(f"{key:<12}: {value}")

        print("=" * 35)