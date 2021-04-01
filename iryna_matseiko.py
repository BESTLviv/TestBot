import datetime
import telebot
from telebot import types

#t.me/testlab1bot

bot = telebot.TeleBot('')
photo_s = 0


def null(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)


@bot.message_handler(commands=["start"])
def start(message):
    now = datetime.datetime.now()
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Нажми на мене", callback_data='start')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Привіт ' + str(message.from_user.username)
                     + ' ! Це повідомлення було відправлено о ' + null(now.hour) + ':' + null(now.minute), reply_markup=keyboard)


@bot.message_handler(commands=["location"])
def access(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_location = types.KeyboardButton('Ваша локація', request_location=True)
    button_contact = types.KeyboardButton('Ваш контакт', request_contact=True)
    keyboard .add(button_location, button_contact)
    bot.send_message(message.chat.id, "Ваші дані", reply_markup=keyboard)


@bot.message_handler(content_types=['photo'])
def photo(message):
    global photo_s
    photo_s = message.json['photo'][0]['file_id']
    bot.send_message(message.chat.id, photo_s)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == 'фото':
        if photo_s == 0:
            bot.send_message(message.chat.id, "А немає класного фото(")
        else:
            bot.send_photo(message.chat.id, photo_s)
    else:
        bot.send_message(message.chat.id, "🐷")


bot.polling(none_stop=True)
