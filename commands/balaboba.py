from email import message
from balaboba import Balaboba
import telebot
from util.bot import bot

hide = False
command = 'balaboba'
description = 'I will continue your text'

bb = Balaboba()
intros = next(bb.intros(language=["en", "ru"]))

@bot.message_handler([command])
def balaboba(msg: telebot.types.Message):
    try:
        return bot.send_message(msg.chat.id, bb.balaboba(telebot.util.extract_arguments(msg.text), intro=intros.number))
    except Exception as e:
        return bot.send_message(msg.chat.id, e)