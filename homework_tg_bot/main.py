from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

TOKEN = '5742785255:AAGfKKBs3mKhaNiY2Q01Zt_L9cKROccWmVQ'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

A = 0
B = 1



def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Здравствуйте!')
    return A


def filt_abv(update, context):
    text = update.message.text.split()
    temp = []
    for i in text:
        if 'абв' not in i.lower():
            temp.append(i)
    context.bot.send_message(update.effective_chat.id, ' '.join(temp[1:]))

def need_game(update, context):
    context.bot.send_message(update.effective_chat.id, 'Не хоти те ли сиграть в игру?')
    text = update.message.text
    if 'да' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Отлично, приступим!')
        return B

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Жаль.')
    return ConversationHandler.END

def game(update, context):
    count_of_sticks = 120
    gamer_1 = 'Игрок'
    gamer_2 = 'Bot'
    current_gamer = gamer_1
    number_to_delete = 1
    while count_of_sticks > 0:
        context.bot.send_message(update.effective_chat.id, f'количество оставшихся палочек: {count_of_sticks}')
        while True:
            if current_gamer == gamer_1:
                context.bot.send_message(update.effective_chat.id, 'Ваш ход (1 - 28): ')
                number_to_delete = update.message.text
                if 1 <=  int(number_to_delete) <= 28:
                    break
            elif current_gamer == gamer_2:
                if count_of_sticks < 29:
                    number_to_delete = 28
                elif 28 < count_of_sticks < 57:
                    number_to_delete = count_of_sticks - 29
                else:
                    number_to_delete = randint(1, 29)
                context.bot.send_message(update.effective_chat.id, f'Мой ход: (1 - 28): {number_to_delete}')
                break
        count_of_sticks -= number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    current_gamer = gamer_1 if current_gamer == gamer_2 else gamer_2
    context.bot.send_message(update.effective_chat.id, f'Победил {current_gamer}')

start_handler = CommandHandler('start', start)
need_game_handler = MessageHandler(Filters.text, need_game)
game_handler = CommandHandler('game', game)
dispatcher.add_handler(game_handler)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={A: [need_game_handler],
                                           B: [game_handler]},
                                   fallbacks=[cancel])
dispatcher.add_handler(conv_handler)

filt_handler = CommandHandler('fil', filt_abv)
dispatcher.add_handler(filt_handler)

updater.start_polling()
updater.idle()
