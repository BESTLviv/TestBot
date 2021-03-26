import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot('1750458289:AAGwuYe-RcrTg9FTLzEQBFHepsPp22s-xyE')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_start = types.InlineKeyboardButton(text='START', callback_data='start')

    markup_inline.add(item_start)

    bot.send_message(message.chat.id, 'Привіт {username}! Це повідомлення було відправлено о {time}.'.format(
        username=message.from_user.username, time=datetime.fromtimestamp(message.date).strftime('%H:%M:%S')),
                     reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def start_answer(call):
    if call.data == 'start':
        bot.send_message(call.message.chat.id, call.data)


@bot.message_handler(commands=['location'])
def location_message(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_location = types.KeyboardButton('Моя локація')
    item_contact = types.KeyboardButton('Мій номер')

    markup_reply.add(item_location, item_contact)
    bot.send_message(message.chat.id, 'Оберіть варіант', reply_markup=markup_reply)



photo = None


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    global photo
    photo = message.photo[0].file_id
    bot.send_message(message.chat.id, photo)


@bot.message_handler(content_types=['text'])
def send_photo(message):
    if message.text == 'Фото':
        if photo is None:
            bot.send_message(message.chat.id, 'А нема.')
        else:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'Моя локація':
        bot.send_message(message.chat.id, 'Десь та й є.')
    elif message.text == 'Мій номер':
        bot.send_message(message.chat.id, 'А який?')


if __name__ == "__main__":
    bot.polling(none_stop=True)
