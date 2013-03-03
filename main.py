from lib.bot import Bot
from util.prompter import Prompter

prompter = Prompter()
bot = Bot(prompter)

bot.start()
