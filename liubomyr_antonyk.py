import telebot, time
from telebot import types

bot = telebot.TeleBot('1744669368:AAEmRWzQ6enY7P061NAIa3e-Rm8VUFVpyCY')

photoID = "NULL"

@bot.message_handler(commands=['start'])
def start_message(message):
    tmsg = lambda x: time.strftime("%H:%M", time.localtime(x))
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text = "Нажми на кнопку.",callback_data= 'true')
    markup.add(button)
    bot.send_message(message.chat.id, "Привіт, {0.first_name}! Це повідомлення було відправлено о ".format(message.from_user)+tmsg(message.date),
    reply_markup=markup)

@bot.message_handler(commands=['location'])
def local_message(message):
    markup = types.ReplyKeyboardMarkup(row_width= 1)
    button1 = types.KeyboardButton('Ваша локація',request_location=True)
    button2 = types.KeyboardButton('Ваш контакт',request_contact=True)
    markup.add(button1,button2)
    bot.send_message(message.chat.id, "Виберіть варіант", reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def result(call):
    if(call.data == 'true'):
        bot.send_message(call.from_user.id,call.data)

@bot.message_handler(content_types=['photo'])
def photo(message):
    global photoID 
    photoID = message.json['photo'][0]['file_id']
    bot.send_message(message.chat.id,"ID фото - "+photoID)
    
@bot.message_handler(content_types=['text'])
def sendphoto(message):
    if(message.text.lower() == "фото"):
        if(photoID != 'NULL'):
            bot.send_photo(message.chat.id ,photoID)
        else:
            bot.send_message(message.chat.id, "Помилка! Немає фото.")
    else:
        bot.send_message(message.chat.id, "Шота на татарском.")

bot.polling()