#! /usr/bin/python3
import os.path
import sys
import json

import telebot

from core import *


# TODO:
# weather: choose different location if more with the same name
# trains: add feature
# timetable: add feature


try:
    with open(os.path.join(os.path.dirname(__file__), '..', 'config.json')) as config:
        try:
            config = json.load(config)
            bot = telebot.TeleBot(config[sys.argv[1]])
            weather_key = config['weather_key']
        except (IndexError, KeyError):
            print('###################################################')
            print('# Please setup the needed keys in the config file #')
            print('###################################################')
            sys.exit()
except FileNotFoundError:
    print('######################################')
    print('# Please provide a valid config file #')
    print('######################################')
    sys.exit()


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, WELCOME_MESSAGE)
    pass


@bot.message_handler(commands=['weather'])
def handle_weather(message):
    message_text = message.text.replace('/weather', '').strip().split()
    try:
        location_name = message_text[0].strip()
    except IndexError:
        location_name = 'Novara'
    try:
        time = message_text[1].strip()
    except IndexError:
        time = 'current'
    bot.reply_to(message, weather(weather_key, location_name, time))
    pass


bot.polling()
