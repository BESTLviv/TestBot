import datetime
import telebot


API_TOKEN = None
with open("token.txt") as tokenFile:
    API_TOKEN = tokenFile.read().strip()

bot = telebot.TeleBot(API_TOKEN)
photo = None

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'inline_text':
        bot.send_message(call.message.chat.id, 'BEST LVIV TOP !!! BEST LVIV TOP !!! BEST LVIV TOP')


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    key1 = telebot.types.InlineKeyboardButton(text='BEST LVIV TOP', callback_data='inline_text')
    keyboard.add(key1)
    date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    msg = "Привіт " + message.from_user.username + " ! Це повідомлення було відправлено о " + date_time
    bot.send_message(message.chat.id, text=msg, reply_markup = keyboard)


@bot.message_handler(commands=['location'])
def location_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button1 = telebot.types.KeyboardButton('Share contact', request_contact=True)
    button2 = telebot.types.KeyboardButton('Share location', request_location=True)
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id, text='Choose option to share', reply_markup=keyboard)


@bot.message_handler(content_types=['photo'])
def photo_id(message):
    photo_id = message.photo[-1].file_id
    global photo
    photo = photo_id
    bot.send_message(message.chat.id, 'ID of your photo is ' + photo_id)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Фото':
        global photo
        if photo is not None:
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, 'Фото відсутнє')


bot.polling(none_stop=True)
