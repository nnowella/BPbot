import telebot
from telebot import types

token = ""

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Найти контакт🔍"))
    bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}</b>\n \nЭтот бот открывает вам доступ к контактам учителей <u>Школы №1561</u>🚀\n \nДля того, чтобы продолжить - используйте <u>кнопку внизу</u>⬇️", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, search)

def com_search(message):
    markup = types.ReplyKeyboardMarkup()
    bp_subject = types.KeyboardButton("По Предмету📚")
    markup.row(bp_subject)
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
    bot.register_next_step_handler(message, selection2)

def selection2(message): 
    if message.text == "Отмена↩️":
        com_search(message)
    else:
        teacher(message)

def teacher(message):
    markup = types.ReplyKeyboardMarkup()
    body = message.text
    if body == "Русский язык":
        t_ruslit = types.KeyboardButton("Сурадеева Ирина Геннадьевна")
        markup.row(t_ruslit)
    if body == "Математика":
        s_mat1 = types.KeyboardButton("Юркевич Дмитрий Евгеньевич")
        s_mat2 = types.KeyboardButton("Слуцкий Леонид Борисович")
        markup.row(s_mat1, s_mat2)
    if body == "Информатика":
        t_inf1 = types.KeyboardButton("Коновалова Татьяна Александровна")
        t_inf2 = types.KeyboardButton("Кондрухова Ольга Васильевна")
        t_inf3 = types.KeyboardButton("Горошко Евгений Валерьевич")
        markup.row(t_inf1, t_inf2, t_inf3)
    if body == "Физика":
        s_fiz1 = types.KeyboardButton("Горбунова Наталья Сергеевна")
        s_fiz2 = types.KeyboardButton("Перепелицын Сергей Анатольевич")
        markup.row(s_fiz1, s_fiz2)
    if body == "Иностранный язык":
        s_forlan1 = types.KeyboardButton("Моргуненко Елена Юрьевна")
        s_forlan2 = types.KeyboardButton("Карпова Анна Сергеевна")
        markup.row(s_forlan1, s_forlan2)
    if body == "Биология и Химия":
        t_biochem = types.KeyboardButton("Кирсанова Наталья Алексеевна")
        markup.row(t_biochem)
    if body == "Обществознание и История":
        t_sochis = types.KeyboardButton("Баженов Олег Александрович")
        markup.row(t_sochis)
    if body == "География":
        t_geo = types.KeyboardButton("Стрижакова Виктория Леонидовна")
        markup.row(t_geo)
    if body == "ОБЖ":
        t_obj = types.KeyboardButton("Теряев Александр Иванович")
        markup.row(t_obj)
    t_cancel = types.KeyboardButton("Отмена↩️")
    markup.row(t_cancel)
    bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, selection3)

def selection3(message):
    if message.text == "Отмена↩️":
        subject(message)
    else:
        t_correlation(message)

def t_correlation(message):
    markup = types.ReplyKeyboardMarkup()
    body = message.text
    if body == "Сурадеева Ирина Геннадьевна":
        bot.send_message(message.chat.id, "<b>Сурадеева Ирина Геннадьевна:</b>\nПочта: - \nТелеграмм: -", parse_mode='html', reply_markup = markup)
    if body == "Юркевич Дмитрий Евгеньевич":
        bot.send_message(message.chat.id, "<b>Юркевич Дмитрий Евгеньевич:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Слуцкий Леонид Борисович":
        bot.send_message(message.chat.id, "<b>Слуцкий Леонид Борисович:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Коновалова Татьяна Александровна":
        bot.send_message(message.chat.id, "<b>Коновалова Татьяна Александровна:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Кондрухова Ольга Васильевна":
        bot.send_message(message.chat.id, "<b>Кондрухова Ольга Васильевна:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Горошко Евгений Валерьевич":
        bot.send_message(message.chat.id, "<b>Горошко Евгений Валерьевич:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Горбунова Наталья Сергеевна":
        bot.send_message(message.chat.id, "<b>Горбунова Наталья Сергеевна:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Перепелицын Сергей Анатольевич":
        bot.send_message(message.chat.id, "<b>Перепелицын Сергей Анатольевич:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Моргуненко Елена Юрьевна":
        bot.send_message(message.chat.id, "<b>Моргуненко Елена Юрьевна:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Карпова Анна Сергеевна":
        bot.send_message(message.chat.id, "<b>Карпова Анна Сергеевна:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Кирсанова Наталья Алексеевна":
        bot.send_message(message.chat.id, "<b>Кирсанова Наталья Алексеевна:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Баженов Олег Александрович":
        bot.send_message(message.chat.id, "<b>Баженов Олег Александрович:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Стрижакова Виктория Леонидовна":
        bot.send_message(message.chat.id, "<b>Стрижакова Виктория Леонидовна:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Теряев Александр Иванович":
        bot.send_message(message.chat.id, "<b>Теряев Александр Иванович:</b>\nПочта: - \nТелеграмм: - ", parse_mode='html', reply_markup = markup)
    if body == "Отмена↩️":
        start(message)
    c_cancel = types.KeyboardButton("Отмена↩️")
    markup.row(c_cancel)
    bot.register_next_step_handler(message, cancelation)

def cancelation(message):
    if message.text == "Отмена↩️":
        teacher(message)
    else:
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, "<b>ОШИБКА</b>", parse_mode='html', reply_markup = markup)

bot.infinity_polling()