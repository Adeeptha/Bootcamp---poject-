import requests
# import os
from datetime import datetime

file = open("file.txt", "w")

api_key = '5ee9db29778e3ceaea3db9fcec7f652b'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

file.write("\n-------------------------------------------------------------")
file.write(str("\nWeather Stats for - {}  || {}".format(location.upper(), date_time)))
file.write("\n-------------------------------------------------------------")

file.write(str("\nCurrent temperature is: {:.2f} deg C".format(temp_city)))
file.write(str("\nCurrent weather desc  :" +weather_desc))
file.write(str("\nCurrent Humidity      :"))
file.write(str( hmdt))
file.write('%')
file.write(str("\nCurrent wind speed    :"))
file.write(str( wind_spd))
file.write('kmph')
file.close()
