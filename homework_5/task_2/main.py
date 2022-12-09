def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-------------')

def take(player):
    flag = False
    while not flag:
        player_answer = input('Куда ставить ' + player+'?: ')
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Введите число от 1 до 9 чтобы походить.')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in 'XO'):
                board[player_answer-1] = player
                flag = True
            else:
                print('Эта клеточка уже занята')
        else:
            print('Некорректный ввод. Введите число от 1 до 9 чтобы походить.')

def win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    flag = False
    while not flag:
        draw_board(board)
        if counter % 2 == 0:
            take('X')
        else:
            take('O')
        counter += 1
        if 4 < counter < 9:
            tmp = win(board)
            if tmp:
                print(tmp, 'выиграл!')
                flag = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(board)

board = list(range(1, 10))

main(board)
