import requests

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

# To use the function and get the weather description:
weather_description = fetch_weather()
if weather_description:
    print(f'Weather: {weather_description}')
