from telebot import types
from util.bot import bot

hide = False
command = 'dice'
description = 'Return dice'

@bot.message_handler([command])
def dice(msg: types.Message):
    bot.send_dice(msg.chat.id)