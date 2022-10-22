from telebot import types
from util.bot import bot

hide = False
command = 'dice'
description = 'Throws the dice'

@bot.message_handler([command])
def dice(msg: types.Message):
    try:
        bot.send_dice(msg.chat.id)
    except Exception as e:
        return bot.send_message(msg.chat.id, e)