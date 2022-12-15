import request, db

def main():
    ansver = 1
    while ansver:
        ansver = request.action()
        if ansver == 1:
            data = db.data_collector()
            db.db_save(data)

        if ansver == 2:
            db_view = request.db_view()
            db.db_print(db_view)

if __name__ == '__main__':
    main()
