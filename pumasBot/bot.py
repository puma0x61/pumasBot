import telebot
import json

TOKEN = '860774372:AAE3yanl0Rl89rXaM34zaSvxbg6d3WMRNWA'

bot = telebot.TeleBot(TOKEN)

welcome_message = 'Welcome!\nThis bot was only built for his uselessnes, DO NOT try to use it with a purpose'
sbabba_msg = 'blblblblblblblblblb ' + u'\U0001F61D'
sbabba_photo = '/spam ' + u'\U0001F621'

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if(message.from_user.username == 'BarbaraMartinengo'):
        bot.reply_to(message, sbabba_msg)
    pass

@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    if(message.from_user.username == 'BarbaraMartinengo'):
        bot.reply_to(message, sbabba_photo)
    pass

bot.polling()

