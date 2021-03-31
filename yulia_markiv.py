import datetime
import requests
from requests.sessions import Request
import telebot
from telebot.apihelper import get_chat_member, get_me, send_message
from telebot import types
from telebot.types import ChatPhoto, Document, InlineKeyboardButton, InputMediaPhoto, KeyboardButton, Location, Message, PhotoSize, ReplyKeyboardMarkup

bot = telebot.TeleBot('1712945168:AAHk3KeM_4CVD05PA1fwPHg_5iaMAiVSkRc')



@bot.message_handler(commands=['start']) # task 2
def start_message(message):
    
    markup_inline = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(text = 'Привіт' , callback_data= 'Hello')
    markup_inline.add(item)
    bot.send_message(message.chat.id,  'Привіт ' + message.from_user.username + '!' + ' Це повідомлення було відправлено о ' + 
    datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') , reply_markup= markup_inline)

@bot.callback_query_handler(func = lambda call : True) #task 5 
def answer(call):
    if call.data == 'Hello':
        bot.send_message(call.message.chat.id , 'Привіт! Як справи ?')



@bot.message_handler(commands = ['location']) #task 6
def start_message(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id , 'Вибери опцію' , reply_markup= keyboard1 )
    button_geo = types.KeyboardButton(text="Відправити місцезнаходження", request_location=True)
    keyboard1.add(button_geo)
    button_cont = types.KeyboardButton(text ="Відправити контакт" , request_contact=True)
    keyboard1.add(button_cont)



FileID = None

@bot.message_handler(content_types =['photo']) # task 3
def message1(message):
        fileID = message.photo[-1].file_id
        #fileID = message.json['photo'][0]['file_id']
        bot.send_message(message.chat.id ,fileID)
        global FileID
        FileID = fileID
        return FileID
        
    

    

@bot.message_handler(content_types='text') #task4
def send_photo(message):
    if message.text.lower() == 'фото':
        if FileID is not None:
            bot.send_photo(message.chat.id ,  FileID )
        else:
           bot.send_message(message.chat.id,  'Ви не надсилали жодного фото ')

   
bot.polling()