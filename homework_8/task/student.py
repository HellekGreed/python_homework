import requests, db

def view_grade():
    person = input('Введите фамилию: ')
    change = requests.change_subject()
    if change == 1:
        d = db.db_read(person)
        for key in d:
            print(f'{key}: {d[key]}')
    if change == 2:
        subject = input('Введите название предмета: ')
        d = db.db_read(person)
        print(f'{subject}: {d[subject]}')