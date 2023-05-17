import telebot
import json
from telebot import types
import requests
from urllib3.exceptions import InsecureRequestWarning

API_URL = 'https://7012.deeppavlov.ai/model'
API_TOKEN='5860976679:AAG7VdNtdfuSCvLX8IuXj_kebU0RmXucl30'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])
def answer(message):
   if message.text == '/wiki':
        bot.send_message(message.chat.id, 'Введите что хотите узнать в wiki')
        bot.register_next_step_handler(message, question) 
   else:
       bot.send_message(message.chat.id, 'Набирите /wiki чтобы узнать что нибуть')
    
def question(message):
    quest = message.text.split()
    quest = " ".join(quest)
    data = {'question_raw': [quest]}
    try:
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        result = requests.post(API_URL,json = data, verify = False).json()
        bot.send_message(message.chat.id, result)
    except:
        bot.send_message(message.chat.id, 'Увы, я это не знаю')


if __name__ == '__main__':
  bot.polling(none_stop=True)