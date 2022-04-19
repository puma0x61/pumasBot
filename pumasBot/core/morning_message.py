from .weather import weather
from .trains import train_delay


def morning_message_creator(weather_key, location_name, train_id):
    weather_ = weather(weather_key, location_name, time='daily')
    train_delay_ = train_delay(train_id)
    morning_message = f'Good morning!\n\n{weather_}.\n\nYour train has a delay of <b>{train_delay_} minutes</b>.'
    return morning_message
