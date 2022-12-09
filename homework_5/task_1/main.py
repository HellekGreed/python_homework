import random

def player_vs_player():

    count_of_sticks = 120
    gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
    current_gamer = gamer_1
    while count_of_sticks > 0:
        print(f'количество оставшихся палочек: {count_of_sticks}')
        while True:
            number_to_delete = int(input(f'ход игрока {current_gamer} (1 - 28): '))
            if 1 <=  number_to_delete <= 28:
                break
        count_of_sticks -= number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    current_gamer = gamer_1 if current_gamer == gamer_2 else gamer_2
    print(f'Победил {current_gamer}')

def player_vs_bot():

    count_of_sticks = 120
    gamer_1 = input('введите имя игрока: ')
    gamer_2 = 'Bot'
    current_gamer = gamer_1
    while count_of_sticks > 0:
        print(f'количество оставшихся палочек: {count_of_sticks}')
        while True:
            if current_gamer == gamer_1:
                number_to_delete = int(input(f'ход игрока {current_gamer} (1 - 28): '))
                if 1 <=  number_to_delete <= 28:
                    break
            elif current_gamer == gamer_2:
                number_to_delete = random.randint(1, 29)
                print(f'ход игрока {current_gamer} (1 - 28): ', number_to_delete)
                if 1 <= number_to_delete <= 28:
                    break
        count_of_sticks -= number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    current_gamer = gamer_1 if current_gamer == gamer_2 else gamer_2
    print(f'Победил {current_gamer}')

def main():
    while True:
        choice = int(input('Введите:\n1 что бы сиграть против другова игрока\n2 что бы сиграть с ботом\nЛюбую другую клавишу что бы выйти\n'))
        if choice == 1:
            player_vs_player()
        elif choice == 2:
            player_vs_bot()
        else:
            break

main()
