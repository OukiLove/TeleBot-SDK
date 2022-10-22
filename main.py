import importlib
import telebot
import os
from util.bot import bot

commands = [] 

for root, dirs, files in os.walk("./commands/"):
    for filename in files:
        if filename.endswith(".py"):
            import_commands = importlib.import_module(f'commands.{filename.split(".py")[0]}')
            if hasattr(import_commands, 'hide') or hasattr(import_commands, 'command') or hasattr(import_commands, 'description'):
                if not import_commands.hide:
                    commands.append(telebot.types.BotCommand(import_commands.command, import_commands.description))

bot.set_my_commands(commands=commands)

bot.polling(non_stop=True)