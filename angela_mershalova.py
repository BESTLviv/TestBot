import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('1726800780:AAGaQ8RsjCphahcFAWh7FAdFFHH-GAovPCw')
# t.me/taskilkimoznabot


@bot.message_handler(commands=['start'])  # task 2
def start_message(message):
    markup_inline = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(text='Inline button', callback_data='Hello')
    markup_inline.add(item)
    bot.send_message(message.chat.id, 'Привіт @'+str(message.from_user.username)
                     + ' це повідомлення було відправлено о '
                     + datetime.datetime.fromtimestamp(message.date).strftime('%H:%M:%S'), reply_markup=markup_inline)


@bot.message_handler(commands=['location'])  # task 6
def location_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('contact', request_contact=True)
    btn2 = types.KeyboardButton('location', request_location=True)
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Choose option:", reply_markup=markup)


Photo_id = None


@bot.message_handler(content_types=['photo'])  # task 3
def photo_message(message):
    photo_id = message.json['photo'][0]['file_id']
    bot.send_message(message.chat.id, 'photo id ' + photo_id)
    global Photo_id
    Photo_id = photo_id
    return Photo_id


@bot.message_handler(content_types=['text'])  # task 4
def text_photo(message):
    if message.text.lower() == 'фото':
        if Photo_id is not None:
            bot.send_photo(message.chat.id,  Photo_id)
        else:
            bot.send_message(message.chat.id,  'Немає фото')


@bot.callback_query_handler(func=lambda call: True)  # task 5
def answer(call):
    if call.data == 'Hello':
        bot.send_message(call.message.chat.id, 'Привіт)')


bot.polling()
