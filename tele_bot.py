# -*- coding: utf-8 -*-
"""Untitled32.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h8BJweVdnOrqdNLtn_HpwyLrD8WICTjT
"""



import telebot
from Adafruit_IO import Client, Feed, Block, Dashboard, Layout,Data, RequestError
user = 'MiiiTiii'
password = 'aio_tbcZ11Oo04K2DL5ptYDMvISW5ZCc'
API_TOKEN = '5262697766:AAFMVnsO5lzhRrWZ7ao1pvL9HdNcre5U67o'

aio = Client(user , password)

try:
    light = aio.feeds('light')
except RequestError:
    feed = Feed(name="light" , visibility = True)
    light = aio.create_feed(feed)
Lamp = True

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start' , 'help'])
def say_hello(message):
  bot.reply_to(message , "Hi, Would you like to turn on or turn off the light?!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):

  if str(message.text) == 'on':
    lamp = True
    Lamp = True
  elif str(message.text) == 'off':
    lamp = False
    Lamp = True
  else :
    bot.reply_to(message , "Just Say OFF or ON , idiot")
    Lamp = False
  if Lamp:
    if lamp :
      aio.send_data(light.key, "#FFFFFF")
      bot.send_photo(message.chat.id, 'https://cdn1.vectorstock.com/i/1000x1000/05/10/3d-realistic-turning-on-light-bulb-icon-vector-28050510.jpg')
    else:
      aio.send_data(light.key, "#000000")
      bot.send_photo(message.chat.id, 'https://w7.pngwing.com/pngs/861/280/png-transparent-incandescent-light-bulb-lamp-turn-off-white-text-hand.png')

# and here we actually run it
bot.polling()

