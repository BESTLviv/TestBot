import telebot
import datetime
import json

bot = telebot.TeleBot('1770075629:AAHVJwdxdrlq8U7Fo6su-wPGcv8cV1wdlFQ')
now = datetime.datetime.now()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт ' + message.from_user.username +'! Це повідомлення було відправлено о ' + str(now))

File_ID = None
file_id = None
@bot.message_handler(content_types=['photo'])
def photo(message):
   file_id = message.photo[2].file_id
   bot.send_message(message.chat.id, file_id)
   #print (file_id)
   global File_ID
   File_ID = file_id
   ##return File_ID

@bot.message_handler(content_types=['text'])
def text(message):
   if message.text == 'Фото': 
       if File_ID == None:
           bot.send_message(message.chat.id, 'На жаль, у нас немає вашого фото :(')
       else: bot.send_photo(message.chat.id, File_ID)
bot.polling()