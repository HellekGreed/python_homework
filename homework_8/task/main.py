import requests, db, student, teacher

def main():
    flag = requests.change_menu()
    while flag:
        account = requests.change_accaunt()
        if account == 1:
            change = requests.teacher_function()
            if change == 1:
                teacher.grade_append()
            if change == 2:
                student.view_grade()
        if account == 2:
            student.view_grade()

        flag = requests.change_rework()

if __name__ == '__main__':
    main()