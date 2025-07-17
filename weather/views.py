# views.py
import requests
from django.http import JsonResponse
from django.views import View
from django.conf import settings

class WeatherView(View):
    def get(self, request, city):
        api_key = settings.WEATHER_API_KEY  # Store API key in settings.py
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                return JsonResponse({"error": data.get("message", "City not found.")}, status=404)

            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }

            return JsonResponse(weather)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
