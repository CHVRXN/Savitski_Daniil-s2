import telebot
from telebot import types

bot = telebot.TeleBot('5110925989:AAEJdiQM9R3m0T6cgWzPskEuawEXit4X9Xg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Lina')
    btn2 = types.KeyboardButton('Legion Commander')
    btn3 = types.KeyboardButton('Terrorblade')
    btn4 = types.KeyboardButton('Techies')
    btn5 = types.KeyboardButton('Shadow Fiend')
    btn6 = types.KeyboardButton('Phantom Assassin')
    btn7 = types.KeyboardButton('Crystal Maiden')
    btn8 = types.KeyboardButton('Zeus')
    btn9 = types.KeyboardButton('Monkey King')
    btn10 = types.KeyboardButton('Juggernaut')
    btn11 = types.KeyboardButton('Io')
    btn12 = types.KeyboardButton('Pudge')
    btn13 = types.KeyboardButton('Rubick')
    btn14 = types.KeyboardButton('Earthshaker')
    btn15 = types.KeyboardButton('Ogre Magi')
    btn16 = types.KeyboardButton('Wraith King')
    btn17 = types.KeyboardButton('Queen of Pain')
    btn18 = types.KeyboardButton('Windranger')
    btn19 = types.KeyboardButton('Spectre')
    btn20 = types.KeyboardButton('Drow Ranger')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
               btn17, btn18, btn19, btn20)
    send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nКакой герой тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "Выбрать другого героя":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Lina')
        btn2 = types.KeyboardButton('Legion Commander')
        btn3 = types.KeyboardButton('Terrorblade')
        btn4 = types.KeyboardButton('Techies')
        btn5 = types.KeyboardButton('Shadow Fiend')
        btn6 = types.KeyboardButton('Phantom Assassin')
        btn7 = types.KeyboardButton('Crystal Maiden')
        btn8 = types.KeyboardButton('Zeus')
        btn9 = types.KeyboardButton('Monkey King')
        btn10 = types.KeyboardButton('Juggernaut')
        btn11 = types.KeyboardButton('Io')
        btn12 = types.KeyboardButton('Pudge')
        btn13 = types.KeyboardButton('Rubick')
        btn14 = types.KeyboardButton('Earthshaker')
        btn15 = types.KeyboardButton('Ogre Magi')
        btn16 = types.KeyboardButton('Wraith King')
        btn17 = types.KeyboardButton('Queen of Pain')
        btn18 = types.KeyboardButton('Windranger')
        btn19 = types.KeyboardButton('Spectre')
        btn20 = types.KeyboardButton('Drow Ranger')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                   btn16, btn17, btn18, btn19, btn20)

        final_message = "Выбрать другого героя"
    elif get_message_bot == 'lina':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Информация о герое", url="https://dota2.fandom.com/ru/wiki/Lina"))
        final_message = "Многие знают, что волосы Lina благословлены огнём, но лишь некоторые знают, почему. Когда " \
                        "Lina была ещё совсем молодой, именно дымящиеся и тлеющие волосы были первым признаком того, " \
                        "что она обладает огромной силой. Потребовались годы усердных тренировок, чтобы волшебница " \
                        "смогла контролировать подобные проявления своего таланта. Но, тем не менее, эту силу нельзя " \
                        "скрывать вечно, и в самые напряжённые моменты битвы волосы Lina вспыхивают, " \
                        "показывая абсолютную концентрацию и высшую степень владения пламенем, которое способно " \
                        "испепелить всё на своем пути. "

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Lina')
        btn2 = types.KeyboardButton('Legion Commander')
        btn3 = types.KeyboardButton('Terrorblade')
        btn4 = types.KeyboardButton('Techies')
        btn5 = types.KeyboardButton('Shadow Fiend')
        btn6 = types.KeyboardButton('Phantom Assassin')
        btn7 = types.KeyboardButton('Crystal Maiden')
        btn8 = types.KeyboardButton('Zeus')
        btn9 = types.KeyboardButton('Monkey King')
        btn10 = types.KeyboardButton('Juggernaut')
        btn11 = types.KeyboardButton('Io')
        btn12 = types.KeyboardButton('Pudge')
        btn13 = types.KeyboardButton('Rubick')
        btn14 = types.KeyboardButton('Earthshaker')
        btn15 = types.KeyboardButton('Ogre Magi')
        btn16 = types.KeyboardButton('Wraith King')
        btn17 = types.KeyboardButton('Queen of Pain')
        btn18 = types.KeyboardButton('Windranger')
        btn19 = types.KeyboardButton('Spectre')
        btn20 = types.KeyboardButton('Drow Ranger')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,
                   btn16, btn17, btn18, btn19, btn20)
        markup = types.InlineKeyboardMarkup()
        final_message = "ошибка\nВоспользуйся одной из интерактивных кнопок ниже"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
