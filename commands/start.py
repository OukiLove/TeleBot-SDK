from telebot import types
from util.bot import bot

hide = True
command = 'start'
description = 'Greetings'

@bot.message_handler([command])
def start(msg: types.Message):
    try:
        bot.send_message(msg.chat.id, "Hello!")
    except Exception as e:
        return bot.send_message(msg.chat.id, e)