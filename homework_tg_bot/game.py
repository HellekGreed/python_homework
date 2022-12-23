from random import randint

def f(x):
    if  x < 29:
        return 28
    elif 28 < x < 57:
        return x - 29
    else:
        return randint(1, 29)

def game(update, context):
    count_of_sticks = 120
    gamer_1 = 'Вы'
    gamer_2 = 'Bot'
    current_gamer = gamer_1
    while count_of_sticks > 0:
        context.bot.send_message(update.effective_chat.id, f'количество оставшихся палочек: {count_of_sticks}')
        while True:
            if current_gamer == gamer_1:
                context.bot.send_message(update.effective_chat.id, 'Ваш ход (1 - 28): ')
                number_to_delete = int(update.message.text)
                if 1 <=  number_to_delete <= 28:
                    break
            elif current_gamer == gamer_2:
                number_to_delete = f(count_of_sticks)
                context.bot.send_message(update.effective_chat.id, 'Ваш ход: (1 - 28): ', number_to_delete)
                break
        count_of_sticks -= number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    current_gamer = gamer_1 if current_gamer == gamer_2 else gamer_2
    context.bot.send_message(update.effective_chat.id, f'Победил {current_gamer}')