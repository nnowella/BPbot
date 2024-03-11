import telebot
from telebot import types

token = ""

bot = telebot.TeleBot(token=token)

subjects = ['Русский язык и Литература',
            'Математика','Информатика',
            'Физика','Иностранный язык',
            'Биология и Химия',
            'Обществознание и История',
            'География',
            'ОБЖ']

teachers = ['Сурадеева Ирина Геннадьевна',
            'Юркевич Дмитрий Евгеньевич',
            'Слуцкий Леонид Борисович',
            'Коновалова Татьяна Александровна',
            'Кондрухова Ольга Васильевна',
            'Горошко Евгений Валерьевич',
            'Горбунова Наталья Сергеевна',
            'Перепелицын Сергей Анатольевич',
            'Моргуненко Елена Юрьевна',
            'Карпова Анна Сергеевна',
            'Кирсанова Наталья Алексеевна',
            'Баженов Олег Александрович',
            'Стрижакова Виктория Леонидовна',
            'Теряев Александр Иванович']

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Найти контакт🔍"))
    bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}</b>\n \nЭтот бот открывает вам доступ к контактам учителей <u>Школы №1561</u>🚀\n \nДля того, чтобы продолжить - используйте <u>кнопку внизу</u>⬇️", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, search)

def com_search(message):
    markup = types.ReplyKeyboardMarkup()
    bp_initials = types.KeyboardButton("По ФИО👤")
    bp_subject = types.KeyboardButton("По Предмету📚")
    markup.row(bp_initials, bp_subject)
    bp_cancel = types.KeyboardButton("Отмена↩️")
    markup.row(bp_cancel)
    bot.send_message(message.chat.id, "<b>Выберите тип поиска:</b>", parse_mode='html', reply_markup = markup)

@bot.message_handler(commands=['search'])
def search(message):
    if message.text == "Найти контакт🔍":
        com_search(message)
        bot.register_next_step_handler(message, selection)
    else:
        com_search(message)
        selection(message)

def selection(message):
    if message.text == "По Предмету📚":
        subject(message)
    if message.text == "Отмена↩️":
        start(message)

def subject(message):
    markup = types.ReplyKeyboardMarkup()
    s_ruslit = types.KeyboardButton("Русский язык")
    markup.row(s_ruslit)
    s_mat = types.KeyboardButton("Математика")
    s_inf = types.KeyboardButton("Информатика")
    markup.row(s_mat, s_inf)
    s_fiz = types.KeyboardButton("Физика")
    s_forlan = types.KeyboardButton("Иностранный язык")
    markup.row(s_fiz, s_forlan)
    s_biochem = types.KeyboardButton("Биология и Химия")
    s_sochis = types.KeyboardButton("Обществознание и История")
    markup.row(s_biochem, s_sochis)
    s_geo = types.KeyboardButton("География")
    s_obj = types.KeyboardButton("ОБЖ")
    markup.row(s_geo, s_obj)
    s_cancel = types.KeyboardButton("Отмена↩️")
    markup.row(s_cancel)
    bot.send_message(message.chat.id, "<b>Выберите предмет:</b>", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, s_correlation)

def s_correlation(message):
    body = message.text
    for subject in subjects:
        if body == subject:
            teacher(message)

def teacher(message):
    markup = types.ReplyKeyboardMarkup()
    s_mat = types.KeyboardButton("Математика")
    markup.row(s_mat)
    bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, t_correlation)

def t_correlation(message):
    body = message.text
    for teacher in teachers:
        if body == teacher:
            a = 1

bot.infinity_polling()