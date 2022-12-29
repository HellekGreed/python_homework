from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


TOKEN = '5742785255:AAGfKKBs3mKhaNiY2Q01Zt_L9cKROccWmVQ'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def log(update, result):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.id},{update.effective_user.first_name},{update.message.text},{result}\n')
def start(update, context):
    result = f'Привет {update.effective_user.first_name} Введи /menu что бы увидеть список команд.'
    log(update, result)
    context.bot.send_message(update.effective_chat.id, f'Привет {update.effective_user.first_name}\nВведи /menu что бы увидеть список команд.')

def menu(update, context):
    result = '/start /menu /filter - убирает все слова с "абв" /calculator'
    log(update, result)
    context.bot.send_message(update.effective_chat.id, '/start\n/menu\n/filter - убирает все слова с "абв"\n/calculator')

def filt_abv(update, context):
    text = update.message.text.split()
    temp = []
    for i in text:
        if 'абв' not in i.lower():
            temp.append(i)
    context.bot.send_message(update.effective_chat.id, ' '.join(temp[1:]))
    result = ' '.join(temp[1:])
    log(update, result)

def calculator(update, context):
    text = update.message.text.split()
    x = float(text[1])
    y = float(text[3])
    if text[2] == '/':
        context.bot.send_message(update.effective_chat.id, f'{x} {text[2]} {y} = {round(x / y, 2)}')
        result = f'{x} {text[2]} {y} = {round(x / y, 2)}'
    elif text[2] == '*':
        context.bot.send_message(update.effective_chat.id, f'{x} {text[2]} {y} = {round(x * y, 2)}')
        result = f'{x} {text[2]} {y} = {round(x * y, 2)}'
    elif text[2] == '+':
        context.bot.send_message(update.effective_chat.id, f'{x} {text[2]} {y} = {round(x + y, 2)}')
        result = f'{x} {text[2]} {y} = {round(x + y, 2)}'
    elif text[2] == '-':
        context.bot.send_message(update.effective_chat.id, f'{x} {text[2]} {y} = {round(x - y, 2)}')
        result = f'{x} {text[2]} {y} = {round(x - y, 2)}'
    else:
        context.bot.send_message(update.effective_chat.id, 'Неправильный ввод!')
        result = 'Неправильный ввод!'
    log(update, result)


start_handler = CommandHandler('start', start)
filt_handler = CommandHandler('filter', filt_abv)
menu_handler = CommandHandler('menu', menu)
calculator_handler = CommandHandler('calculator', calculator)
dispatcher.add_handler(calculator_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(filt_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
