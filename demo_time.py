import drivers
from time import sleep
from datetime import  datetime
from multiprocessing import Process
import requests

display = drivers.Lcd()
api_key = '46191dbc779cc644b3ef1468a6a5e1a5'
city = 'Struer'

def fetch_weather():
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    try:
        response = requests.get(api_url)
        data = response.json()
        weather = data['weather'][0]['description']
        return weather
    except Exception as e:
        print('Error fetching weather data:', e)

weather_description = fetch_weather()
if weather_description:
    print(f'Weather: {weather_description}')

def updateTime():
    while True:
        now = datetime.now().time()
        display.lcd_display_string(f'    {now.replace(microsecond=0)}',2)
        sleep(1)

p = Process(target=updateTime)

try:
    print("Skriver til LCD skaermen")
    
    p.start()

    while True:
        display.lcd_display_string("   Klokken er:  ", 1)
        sleep(6)
        display.lcd_display_string(f'Weather: {weather_description}', 1)
        sleep(6)

except KeyboardInterrupt:
    print("Slukker for uret")
    display.lcd_clear()