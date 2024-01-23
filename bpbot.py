import telebot
from telebot import types

token = "6927857136:AAFsHm4A-o1zLrKqL2QteMiBvaR0ET-jTnI"

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Найти контакт🔍", callback_data='con'))
    bot.send_message(user, f"<b>Привет, {message.from_user.first_name}</b>\n \nЭтот бот открывает вам доступ к контактам учителей <u>Школы №1561</u>🚀\n \nДля того, чтобы продолжить - используйте <u>кнопку внизу</u>⬇️", parse_mode='html', reply_markup = markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_con(callback):
    if callback.data == 'con':
        contact(callback.message)

@bot.message_handler(commands=['contact'])
def contact(message):
    user = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    button11 = types.KeyboardButton("11-ый")
    markup.row(button11)
    bot.send_message(user, "<b>Начнём</b>\n \nВыберите корпус, в котором вы учитесь🏫", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(user, corpus)
def corpus(message):
    user = message.chat.id
    if message.text() == "11-ый":
        markup = types.ReplyKeyboardMarkup()
        buttonfio = types.KeyboardButton("По ФИО")
        buttonsub = types.KeyboardButton("По Предмету📚")
        markup.row(buttonfio)
        markup.row(buttonsub)
        bot.send_message(user, "<b>Выберите тип поиска:</b>", parse_mode='html', reply_markup = markup)
        bot.register_next_step_handler(user, search)
    def search(message):
        user = message.chat.id
        if message.text() == "По Предмету📚":
            markup = types.InlineKeyboardMarkup()
            b_rus_lit = types.InlineKeyboardButton("Русский язык и Литература", callback_data='ruslit')
            b_mat = types.InlineKeyboardButton("Математика",callback_data='mat')
            markup.row(b_rus_lit, b_mat)
            b_inf = types.InlineKeyboardButton("Информатика", callback_data='inf')
            b_fiz = types.InlineKeyboardButton("Физика", callback_data='fiz')
            markup.row(b_inf, b_fiz)
            b_in_yaz = types.InlineKeyboardButton("Иностранный язык", callback_data='lang')
            b_bio_him = types.InlineKeyboardButton("Биология и Химия", callback_data='biohim')
            markup.row(b_in_yaz, b_bio_him)
            b_obz_ist = types.InlineKeyboardButton("Обществознание и История", callback_data='hist')
            b_geo_obj = types.InlineKeyboardButton("География и ОБЖ", callback_data='geob')
            markup.row(b_obz_ist, b_geo_obj)
            b_cancel = types.InlineKeyboardButton("Отмена↩️", callback_data='cancel')
            markup.row(b_cancel)
            bot.send_message(user, "<b>Выберите предмет:</b>", parse_mode='html', reply_markup = markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_sub(callback):
    user = callback.message.chat.id
    if callback.data == 'ruslit':
        markup = types.InlineKeyboardMarkup()
        rlt1 = types.InlineKeyboardButton("Сурадеева И.Г.", callback_data='rl1')
        markup.row(rlt1)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'mat':
        markup = types.InlineKeyboardMarkup()
        mt1 = types.InlineKeyboardButton("Юркевич Д.Е.", callback_data='mat1')
        mt2 = types.InlineKeyboardButton("Слуцкий Л.Б.", callback_data='mat2')
        markup.row(mt1, mt2)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'inf':
        markup = types.InlineKeyboardMarkup()
        it1 = types.InlineKeyboardButton("Коновалова Т.А.", callback_data='inf1')
        it2 = types.InlineKeyboardButton("Звягинцев Д.А.", callback_data='inf2')
        markup.row(it1, it2)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'fiz':
        markup = types.InlineKeyboardMarkup()
        ft1 = types.InlineKeyboardButton("Горбунова Н.С.", callback_data='fiz1')
        ft2 = types.InlineKeyboardButton("Перепелицын С.А.", callback_data='fiz2')
        markup.row(ft1, ft2)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'lang':
        markup = types.InlineKeyboardMarkup()
        lt1 = types.InlineKeyboardButton("Моргуненко Е.Ю.", callback_data='lan1')
        lt2 = types.InlineKeyboardButton("Карпова А.С.", callback_data='lan2')
        markup.row(lt1, lt2)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'biohim':
        markup = types.InlineKeyboardMarkup()
        bht1 = types.InlineKeyboardButton("Кирсанова Н.А.", callback_data='bio1')
        markup.row(bht1)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'hist':
        markup = types.InlineKeyboardMarkup()
        oht1 = types.InlineKeyboardButton("Баженов О.А.", callback_data='his1')
        markup.row(oht1)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'geob':
        markup = types.InlineKeyboardMarkup()
        gt1 = types.InlineKeyboardButton("Стрижакова В.Л.", callback_data='geo1')
        ot1 = types.InlineKeyboardButton("Теряев А.И.", callback_data='obj1')
        markup.row(rlt1)
        bot.send_message(user, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif callback.data == 'cancel':
        corpus(callback.message)

bot.polling(none_stop=True)
