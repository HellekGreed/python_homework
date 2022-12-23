from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

TOKEN = '5742785255:AAGfKKBs3mKhaNiY2Q01Zt_L9cKROccWmVQ'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher



def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Здравствуйте!')

def filt_abv(update, context):
    text = update.message.text.split()
    temp = []
    for i in text:
        if 'абв' not in i.lower():
            temp.append(i)
    context.bot.send_message(update.effective_chat.id, ' '.join(temp[1:]))

start_handler = CommandHandler('start', start)
filt_handler = CommandHandler('fil', filt_abv)
dispatcher.add_handler(filt_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
