import requests

from .constants import *


def get_weather(weather_key, location_name, exclude='minutely'):
    location = requests.get(
        f'https://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit={LIMIT}&appid={weather_key}'
    ).json()
    lat = location[0]['lat']
    lon = location[0]['lon']
    if exclude == '':
        weather_obj = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={weather_key}'
        ).json()
    else:
        weather_obj = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={weather_key}'
        ).json()
    return weather_obj, location_name


def weather_message_creator(weather_list, time):
    weather_obj, location_name = weather_list[0], weather_list[1]
    alert = ''
    if time == 'current':
        weather_description = weather_obj['current']['weather'][0]['description']
        time_description = f'The current weather for {location_name} is: '
    # elif time == 'minutely':
    #     weather_description = weather['minutely'][0]['weather'][0]['description']
    #     time_description = 'The current weather is '
    elif time == 'hourly':
        weather_description = weather_obj['hourly'][0]['weather'][0]['description']
        time_description = f'The weather in {location_name} the next hour is: '
    elif time == 'daily':
        weather_description = weather_obj['daily'][0]['weather'][0]['description']
        time_description = f'This day\'s weather in {location_name} is: '
    elif time == 'alerts':
        weather_description = weather_obj['alerts'][0]['description']
        alert = weather_obj['alerts'][0]['event']
        time_description = f'⚠ALERT FOR {location_name.upper()}⚠\n\n' + alert + '\n\n'
    else:
        time_description = ''
        weather_description = WEATHER_ERROR
    weather_message = time_description + weather_description
    return weather_message


def weather(weather_key, location_name, time):
    return weather_message_creator(get_weather(weather_key, location_name), time)
