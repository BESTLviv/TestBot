from telebot import TeleBot

API_TOKEN = ""

bot = TeleBot(API_TOKEN)

if __name__ == "__main__":
    bot.polling(none_stop=True)