import telebot
from telebot import types

token = ""

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Найти контакт🔍"))
    bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}</b>\n \nЭтот бот открывает вам доступ к контактам учителей <u>Школы №1561</u>🚀\n \nДля того, чтобы продолжить - используйте <u>кнопку внизу</u>⬇️", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, poisk)

@bot.message_handler(commands=['contact'])
def poisk(message):
    if message.text == "Найти контакт🔍":
        markup = types.ReplyKeyboardMarkup()
        b_fio = types.KeyboardButton("По ФИО👤")
        b_sub = types.KeyboardButton("По Предмету📚")
        markup.row(b_fio, b_sub)
        bot.send_message(message.chat.id, "<b>Выберите тип поиска:</b>", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, search)

def search(message):
    if message.text == "По Предмету📚":
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
        b_cancel1 = types.KeyboardButton("Отмена↩️")
        markup.row(b_cancel1)
        bot.send_message(message.chat.id, "<b>Выберите предмет:</b>", parse_mode='html', reply_markup = markup)
    bot.register_next_step_handler(message, choice)

def choice(message):
    if message.text == "Русский язык и Литература":
        markup = types.ReplyKeyboardMarkup()
        b_rlt1 = types.KeyboardButton("Сурадеева Ирина Геннадьевна")
        markup.row(b_rlt1)
        b_cancel2 = types.KeyboardButton("Отмена↩️")
        markup.row(b_cancel2)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "Математика":
        markup = types.ReplyKeyboardMarkup()
        b_rlt1 = types.KeyboardButton("Сурадеева Ирина Геннадьевна")
        markup.row(b_rlt1)
        b_cancel3 = types.KeyboardButton("Отмена↩️")
        markup.row(b_cancel3)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "Информатика":
        markup = types.ReplyKeyboardMarkup()
        b_it1 = types.KeyboardButton("Коновалова Татьяна Александровна")
        b_it2 = types.KeyboardButton("Звягинцев Дмитрий Александрович")
        markup.row(b_it1, b_it2)
        b_it3 = types.KeyboardButton("Кондрухова Ольга Васильевна")
        b_it4 = types.KeyboardButton("Горошко Евгений Валерьевич")
        markup.row(b_it3, b_it4)
        b_cancel4 = types.KeyboardButton("Отмена↩️")
        markup.row(b_cancel4)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "Физика":
        markup = types.ReplyKeyboardMarkup()
        b_ft1 = types.KeyboardButton("Горбунова Наталья Сергеевна")
        b_ft2 = types.KeyboardButton("Перепелицын Сергей Анатольевич")
        markup.row(b_ft1, b_ft2)
        b_cancel5 = types.KeyboardButton("Отмена↩️")
        markup.row(b_cancel5)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "Иностранный язык":
        markup = types.ReplyKeyboardMarkup()
        b_elt1 = types.KeyboardButton("Моргуненко Елена Юрьевна")
        b_elt2 = types.KeyboardButton("Карпова Анна Сергеевна")
        markup.row(b_elt1, b_elt2)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "Биология и Химия":
        markup = types.ReplyKeyboardMarkup()
        b_bct1 = types.KeyboardButton("Кирсанова Наталья Алексеевна")
        markup.row(b_bct1)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "Обществознание и История":
        markup = types.ReplyKeyboardMarkup()
        b_oht1 = types.KeyboardButton("Баженов Олег Александрович")
        markup.row(b_oht1)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "География и ОБЖ":
        markup = types.ReplyKeyboardMarkup()
        b_gt1 = types.KeyboardButton("Стрижакова Виктория Леонидовна")
        b_ot1 = types.KeyboardButton("Теряев Александр Иванович")
        markup.row(b_gt1, b_ot1)
        bot.send_message(message.chat.id, "<b>Выберите преподавателя:</b>", parse_mode='html', reply_markup = markup)
    elif message.text == "Отмена↩️":
        bot.register_next_step_handler(message, poisk)

bot.polling(none_stop=True)