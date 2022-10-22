from telebot import types
from util.bot import bot

hide = True
command = 'start'
description = 'Return hello!'

@bot.message_handler([command])
def start(msg: types.Message):
    bot.send_message(msg.chat.id, "Hello! Learn commands: /help")