from .weather import weather
from .trains import train_delay
from .lessons import *


def morning_message_creator(weather_key, location_name, train_id):
    weather_message = weather(weather_key, location_name, time='daily')
    train_delay_message = delay_message(train_delay(train_id))
    morning_message = f'Good morning!\n\n{weather_message}.\n\nYour train is {train_delay_message}'
    schedule_message = schedule_message_creator()
    return morning_message, schedule_message


def delay_message(train_delay_minutes):
    if train_delay_minutes < 0:
        train_delay_minutes = abs(train_delay_minutes)
        train_delay_message = f'<b>{train_delay_minutes} minutes</b> early!'
    elif train_delay_minutes > 0:
        train_delay_message = f'delayed by <b>{train_delay_minutes} minutes</b> :(.'
    else:
        train_delay_message = 'on time!'
    return train_delay_message
