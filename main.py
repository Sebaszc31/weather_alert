import requests
import os

TELEGRAM = f"https://api.telegram.org/bot{os.environ.get("TOKEN_TELE")}/sendMessage"

TELEGRAM_PARAMS = {
    "chat_id" : os.environ.get("CHAT_ID"),
    "text" : "It's gonna rain nigga"
}

parameters = {
    "lat" : 6.15350,
    "lon" : -75.580694,
    "appid" : os.environ.get("APPID"),
    "cnt" : 4
}
response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast", params= parameters)

weather_data = response.json()
print(weather_data)

#
#will_rain = False
#for hour_data in weather_data["list"]:
 #   condition_code = hour_data["weather"][0]["id"]
    
 #   if int(condition_code) < 700:
  #      will_rain = True

#if will_rain:
 #   response = requests.get(url= TELEGRAM, params= TELEGRAM_PARAMS)
