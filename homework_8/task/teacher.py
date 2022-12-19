import db

def grade_append():
    question = int(input('1 - Ученик существует в базе\n0 - Cоздать нового ученика\n'))
    student = input('Введите фамилию студента: ')
    subject = input('Введите название предмета: ')
    grade = input('Введите оценку: ')
    if question:
        d = db.db_read(student)
        if d.get(subject) != None:
            d[subject] += ', ' + grade
        else:
            d2 = {subject: grade}
            d.update(d2)
        db.db_save(student, d)
    else:
        d = {subject: grade}
        db.db_save(student, d)

