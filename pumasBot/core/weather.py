import requests

from math import trunc

from .constants import *

# TODO:
# refactor
# move geolocation to new file


def get_weather(weather_key, location_name, exclude='minutely', limit=1, units='metric'):
    location = requests.get(
        f'https://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit={limit}&appid={weather_key}'
    ).json()
    # print(location)
    lat = location[0]['lat']
    lon = location[0]['lon']
    if exclude == '':
        weather_obj = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?'
            f'lat={lat}&lon={lon}&units={units}&appid={weather_key}'
        ).json()
    else:
        weather_obj = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?'
            f'lat={lat}&lon={lon}&exclude={exclude}&units={units}&appid={weather_key}'
        ).json()
    # print(weather_obj)
    return weather_obj, location_name


def weather_message_creator(weather_list, time):
    weather_obj, location_name = weather_list[0], weather_list[1]
    temperature_units = ' degrees celsius'
    try:
        if time == 'current':
            weather_description = weather_obj[time]['weather'][0]['description']
            temperature = weather_obj[time]['temp']
            weather_message = f'In {location_name}, we currently have {weather_description}, ' \
                              f'with a temperature of {str(trunc(temperature)) + temperature_units}'
        # minutely precipitation forecast: will probably never be implemented
        # elif time == 'minutely':
        #     weather_description = weather['minutely'][0]['weather'][0]['description']
        #     time_description = 'The current weather is '
        elif time == 'hourly':
            weather_description = weather_obj[time][0]['weather'][0]['description']
            temperature = weather_obj[time][0]['temp']
            weather_message = f'The weather in {location_name} in the next hour will be {weather_description}, ' \
                              f'with a temperature of {str(trunc(temperature)) + temperature_units}'
        elif time == 'daily':
            weather_description = weather_obj['daily'][0]['weather'][0]['description']
            temperature_avg = weather_obj[time][0]['temp']['day']
            temperature_min = weather_obj[time][0]['temp']['min']
            temperature_max = weather_obj[time][0]['temp']['max']
            weather_message = f'This day\'s weather in {location_name} will be {weather_description}, ' \
                              f'with an average temperature of {str(trunc(temperature_avg)) + temperature_units} ' \
                              f'(min {trunc(temperature_min)}, max {trunc(temperature_max)})'
        elif time == 'alerts':
            weather_description = weather_obj['alerts'][0]['description']
            alert = weather_obj['alerts'][0]['event']
            weather_message = f'⚠ALERT FOR {location_name.upper()}⚠\n\n' + alert + '\n\n' + weather_description
        else:
            weather_message = WEATHER_ERROR
    except KeyError:
        weather_message = WEATHER_KEYERROR
    return weather_message


def weather(weather_key, location_name, time):
    return weather_message_creator(get_weather(weather_key, location_name), time)
