import datetime as dt
import requests
from pushbullet import Pushbullet

URL = "http://api.openweathermap.org/data/2.5/weather?appid=c879f1bcd9ac6696a2231240b4bab3f7&q=Hoddesdon"
response = requests.get(URL).json()

#Get temperature
temp_kelvin = response["main"]["temp"]
temp_celsius = temp_kelvin - 273.15
temp = round(temp_celsius, 0)

#Get other stuff
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise = str(dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"]))
sunset = str(dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"]))

humidity = str(humidity)+"%"
#temperature = str(temp)+"C"
temperature = str(temp)+chr(176)+"C"

sunrise = sunrise.split(" ")
sunrise = sunrise[1]
sunrise = "Sunrise: "+sunrise

sunset = sunset.split(" ")
sunset = sunset[1]
sunset = "Sunset: "+sunset

description = str(description)+"\n"
temperature = str(temperature)+"\n"
sunrise = str(sunrise)+"\n"
sunset = str(sunset)+"\n"
humidity = str(humidity)+"\n"

f = open("data.txt","a")

f.write(description)
f.write(temperature)
f.write(sunrise)
f.write(sunset)
f.write(humidity)
f.close()

with open("data.txt", mode = "r") as f:
    text = f.read()

api_key = ""#Need Pushbullet API Key
pb = Pushbullet(api_key)
push = pb.push_note("Weather", text)

f = open("data.txt","w")
f.write("")
f.close()
