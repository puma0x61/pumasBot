import telebot
import json

TOKEN = '860774372:AAE3yanl0Rl89rXaM34zaSvxbg6d3WMRNWA'

bot = telebot.TeleBot(TOKEN)

welcome_message = 'Welcome!\nThis bot was only built for his uselessnes, DO NOT try to use it with a purpose'

sbabba_msg = 'asdf'

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.from_user.username)
    if(message.from_user.username == 'BarbaraMartinengo'):
        bot.reply_to(message, sbabba_msg)

@bot.message_handler(content_types="sticker")
def handle_sticker(message):
    bot.reply_to(message, "sticker") 

bot.polling()

