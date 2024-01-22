import telebot
from telebot import types

token = "6927857136:AAFsHm4A-o1zLrKqL2QteMiBvaR0ET-jTnI"

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user, f"<b>Привет, {message.from_user.first_name}</b>\n \nЭтот бот открывает вам доступ к контактам учителей <u>Школы №1561</u>🚀", parse_mode='html')

bot.polling(none_stop=True)