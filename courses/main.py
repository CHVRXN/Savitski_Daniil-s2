import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('5291329078:AAHH3Fyda9kEN80liL06kDFiAaYlTQ8GkFI')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    but1 = types.KeyboardButton("Во всём мире")
    but2 = types.KeyboardButton("США")
    but3 = types.KeyboardButton("Россия")
    but4 = types.KeyboardButton("Украина")
    but5 = types.KeyboardButton("Франция")
    but6 = types.KeyboardButton("Китай")
    but7 = types.KeyboardButton("Беларусь")
    but8 = types.KeyboardButton("Италия")
    but9 = types.KeyboardButton("Великобритания")
    markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9)

    send_mess = f"<b>Приветствую {message.from_user.first_name}!</b>\nЭтот бот обладает самой свежей и точной информацией. Не сомневайся!\nЧтобы получить данные по коронавирусу выбери страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "китай":
        location = covid19.getLocationByCountryCode("CN")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "великобритания":
        location = covid19.getLocationByCountryCode("GB")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
