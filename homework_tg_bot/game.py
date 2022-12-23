from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

TOKEN = '5742785255:AAGfKKBs3mKhaNiY2Q01Zt_L9cKROccWmVQ'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

A = 0
B = 1
C = 2

count_of_sticks = 120

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Здравствуйте!\nВведите число от 1 до 28 что бы начать игру ')
    return A

def player_turn(update, context):
    global count_of_sticks
    context.bot.send_message(update.effective_chat.id, f'Ваш ход (1 - 28): {update.message.text}')
    count_of_sticks -= int(update.message.text)
    context.bot.send_message(update.effective_chat.id, f'Осталось: {count_of_sticks}')


    if count_of_sticks > 0:
        context.bot.send_message(update.effective_chat.id, 'Введите что угодно что бы продолжить')
        return B
    else:
        count_of_sticks = 120
        context.bot.send_message(update.effective_chat.id, 'Ты победил!')
        return A
def bot_turn(update, context):
    global count_of_sticks
    if count_of_sticks < 29:
        number_to_delete = count_of_sticks
    elif 28 < count_of_sticks < 57:
        number_to_delete = count_of_sticks - 29
    else:
        number_to_delete = randint(1, 29)
    context.bot.send_message(update.effective_chat.id, f'Мой ход: {number_to_delete}')
    count_of_sticks -= number_to_delete
    context.bot.send_message(update.effective_chat.id, f'Осталось: {count_of_sticks}')

    if count_of_sticks > 0:
        context.bot.send_message(update.effective_chat.id, 'Введите число от 1 до 28')
        return C
    else:
        count_of_sticks = 120
        context.bot.send_message(update.effective_chat.id, 'Я победил!')
        return A

def end(update, context):
    context.bot.send_message(update.effective_chat.id, 'END')
    return ConversationHandler.END




start_handler = CommandHandler('start', start)
player_turn_handler = MessageHandler(Filters.text, player_turn)
bot_turn_handler = MessageHandler(Filters.text, bot_turn)
end_handler = CommandHandler('end', start)


conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={A: [player_turn_handler],
                                           B: [bot_turn_handler],
                                           C: [player_turn_handler]},
                                   fallbacks=[end_handler])
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
