def data_collector():
    s_name = input('Введите фамилию: ')
    f_name = input('Введите имя: ')
    tele = input("Введите телефон: ")
    coment = input('Введите описание телефона(например рабочий): ')
    print()
    data = [s_name, f_name, tele, coment]
    return data

def db_save(data):
    db_column = '\n'.join(data)
    db_column += '\n \n'
    with open('file_column.txt', 'a') as file:
        file.write(db_column)

    db_string = ','.join(data)
    db_string += '\n'
    with open('file_string.txt', 'a') as file:
        file.write(db_string)

def db_print(choise):
    if choise == 1:
        with open('file_column.txt', 'r') as file:
            for line in file:
                print(line, end='')
    if choise == 2:
        with open('file_string.txt', 'r') as file:
            for line in file:
                print(line, end='')

