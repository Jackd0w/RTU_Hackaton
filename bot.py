import telebot
from telebot import types


'''
TODO
Add function to accept code from 
'''


token = "5137080407:AAEb_xcC3J3-TcUAG7nqxNpVEUL2F2dU-9I"

bot = telebot.TeleBot(token, parse_mode=None, )



@bot.message_handler(commands=['help'])
def help_function(message):
    bot.reply_to(message, "help message")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hi")

@bot.message_handler(commands=['button'])
def button_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Кнопка")
  markup.add(item1)

@bot.message_handler(commands=["problems"])
def problems_function(message):
    bot.reply_to(message)




if __name__ == "__main__":
    bot.infinity_polling()