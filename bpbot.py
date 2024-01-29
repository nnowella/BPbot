import telebot
from telebot import types

token = ""

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Найти контакт🔍"))
    bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}</b>\n \nЭтот бот открывает вам доступ к контактам учителей <u>Школы №1561</u>🚀\n \nДля того, чтобы продолжить - используйте <u>кнопку внизу</u>⬇️", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message.chat.id, poisk)

def poisk(message):
    if message.text() == "Найти контакт🔍":
        bot.register_next_step_handler(message.chat.id, contact)

@bot.message_handler(commands=['contact'])
def contact(message):
    markup = types.ReplyKeyboardMarkup()
    button11 = types.KeyboardButton("11-ый")
    markup.row(button11)
    bot.send_message(message.chat.id, "<b>Начнём</b>\n \nВыберите корпус, в котором вы учитесь🏫", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message.chat.id, search)

    def search(chat):
        if chat.text() == "По Предмету📚":
            markup = types.ReplyKeyboardMarkup()
            b_rus_lit = types.KeyboardButton("Русский язык и Литература")
            b_mat = types.KeyboardButton("Математика")
            markup.row(b_rus_lit, b_mat)
            b_inf = types.KeyboardButton("Информатика")
            b_fiz = types.KeyboardButton("Физика")
            markup.row(b_inf, b_fiz)
            b_in_yaz = types.KeyboardButton("Иностранный язык")
            b_bio_him = types.KeyboardButton("Биология и Химия")
            markup.row(b_in_yaz, b_bio_him)
            b_obz_ist = types.KeyboardButton("Обществознание и История")
            b_geo_obj = types.KeyboardButton("География и ОБЖ")
            markup.row(b_obz_ist, b_geo_obj)
            b_cancel = types.KeyboardButton("Отмена↩️")
            markup.row(b_cancel)
            bot.send_message(chat.id, "<b>Выберите предмет:</b>", parse_mode='html', reply_markup = markup)

bot.polling(none_stop=True)