from .weather import weather
from .trains import delay_message
from .lessons import *


def morning_message_creator(weather_key, location_name, train_id):
    weather_message = weather(weather_key, location_name, time='daily')
    train_delay_message = delay_message(train_id)
    morning_message = f'Good morning!\n\n{weather_message}.\n\n{train_delay_message}'
    schedule_message = schedule_message_creator()
    return morning_message, schedule_message
