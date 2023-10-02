# ecdd90bc64a94bbb9e0101110232709  - weather api key
#pip install requests
import requests
import json
import pyttsx3

text_speech = pyttsx3.init()

print("Want to know the current weather")

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=ecdd90bc64a94bbb9e0101110232709&q={city}"
# https://api.weatherapi.com/v1/current.json?key=ecdd90bc64a94bbb9e0101110232709&q=lucknow}

weatherData = requests.get(url)

# first the weather will be display and then system will speak the information
region = weatherData.json()["location"]["region"]
weather = weatherData.json()["current"]["condition"]["text"]
temp = weatherData.json()["current"]["temp_c"]

print(f"The weather in {city} is : {weather}")
text_speech.say(f"Weather in {city} is : {weather}")
text_speech.runAndWait()

print(f"The temperature in {city} is : {temp} °c")
text_speech.say(f"Current Temperature in {city} is : {temp} °c")
text_speech.runAndWait()

print(f"The region is {region}")
text_speech.say(f"Region is {region}")
text_speech.runAndWait()


# print(weather,temp)
# print(weatherData.json())



