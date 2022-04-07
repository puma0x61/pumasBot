#! /usr/bin/python3

import sys
import json

import requests
import telebot

from core import *


# TODO:
# weather: choose different location if more with the same name
# trains: add feature
# timetable: add feature


with open('../config.json') as config:
    config = json.load(config)
    if config['pumasBot']:
        bot = telebot.TeleBot(token=config['pumasBot'])
        weather_key = config['weather_key']
    else:
        print("###################################################")
        print("# Please setup the needed keys in the config file #")
        print("###################################################")
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
        pass
    try:
        time = message_text[1].strip()
    except IndexError:
        time = 'current'
        pass
    bot.reply_to(message, weather(weather_key, location_name, time))
    pass


bot.polling()
