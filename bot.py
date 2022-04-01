from markupsafe import Markup
import telebot
from telebot import types


'''
TODO
Add function to accept code from 
'''


token = "5137080407:AAEb_xcC3J3-TcUAG7nqxNpVEUL2F2dU-9I"

bot = telebot.TeleBot(token, parse_mode=None, )

ids = ["665659475"]

@bot.message_handler(content_types=['text'])
def id_reader(message):
    if message.text in ids:
        return True
    else:
        return False

@bot.message_handler(commands=['start'])
def start_handler(message):
    global ids # массив с айди пользователей, которые допущены
    bot.send_message(message.chat.id, "Привет, введи код, полученный на сайте:")
    if  #исправь на id, когда закончишь
        bot.send_message(message.chat.id, 'Ошибся адресом, дружок')
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤬 Дедлайны")
        btn2 = types.KeyboardButton("❓ Что запланировано на сегодня?")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, который поможет тебе не потеряться среди вечно горящих дедлайнов".format(message.from_user), 
                        reply_markup=markup)




    

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🤬 Дедлайны"):
        bot.send_message(message.chat.id, text="Куча заданий")
    elif(message.text == "❓ Что запланировано на сегодня?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Конкретней про задачи")
        btn2 = types.KeyboardButton("Психологическая помощь")
        btn3 = types.KeyboardButton("Помощь с мотивацией")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="План на сегодня", reply_markup=markup)
    
    elif(message.text == "Конкретней про задачи"):
        bot.send_message(message.chat.id, "Здесь выводим ответ из базы данных")
    
    elif message.text == "Психологическая помощь":
        bot.send_message(message.chat.id, text="Солнце скоро взорвется, ничто не имеет смысла ☠☠🥳🥳")
    elif message.text == "Помощь с мотивацией":
        bot.send_message(message.chat.id, text="Иди работай, чертила 😈😈😈")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🤬 Дедлайны")
        button2 = types.KeyboardButton("❓ Что запланировано на сегодня?")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="🚧CONSTRUCTION ZONE. FEATURES TO BE ADDED🚧")




if __name__ == "__main__":
    bot.infinity_polling()