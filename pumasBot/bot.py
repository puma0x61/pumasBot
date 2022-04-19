#! /usr/bin/python3
import csv
import os.path
import sys
import json
import datetime
import time

import telebot

from core import *


# TODO:
# weather: choose different location if more with the same name
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


try:
    with open(os.path.join(os.path.dirname(__file__), '..', 'users.csv'), newline='') as users_csv:
        users_list = [row for row in csv.DictReader(users_csv)]
except FileNotFoundError:
    print('###########################################################')
    print('# users.csv file not found || can\'t send morning updates #')
    print('###########################################################')


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, WELCOME_MESSAGE, parse_mode='html')
    pass


@bot.message_handler(commands=['weather'])
def handle_weather(message):
    message_text = message.text.replace('/weather', '').strip().split()
    try:
        location_name = message_text[0].strip()
    except IndexError:
        location_name = 'Novara'
    try:
        time_ = message_text[1].strip()
    except IndexError:
        time_ = 'current'
    bot.reply_to(message, weather(weather_key, location_name, time_), parse_mode='html')
    pass


@bot.message_handler(commands=['trains'])
def handle_trains(message):
    try:
        train_id = message.text.split(' ')[1]
        train_message = train_delay(train_id)
    except IndexError:
        train_message = 'Train not found. Check if you have the right train number!'
    bot.reply_to(message, train_message, parse_mode='html')
    pass


def morning_message_sender():
    try:
        for user in users_list:
            chat_id, location_name, train_id = user['chat_id'], user['location_name'], user['train_id']
            bot.send_message(chat_id, morning_message_creator(weather_key, location_name, train_id), parse_mode='html')
    except Exception as e:
        print(e)
        pass
    pass


morning_message_sender()


bot.polling()
