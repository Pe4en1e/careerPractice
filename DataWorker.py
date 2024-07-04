import sqlite3


def createTable():
    try:
        connection = sqlite3.connect('vacancies.db')
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS requests ('
                       'requestText TEXT NOT NULL,'
                       'schedule TEXT NOT NULL,'
                       'experience TEXT NOT NULL,'
                       'found TEXT NOT NULL)')

        connection.commit()
        connection.close()

        return True
    except Exception as e:
        print(e)
        return False



def createRecord(name, sch, exp, found):
    try:
        connection = sqlite3.connect('vacancies.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO requests (requestText, schedule, experience, found) VALUES (?, ?, ?, ?)", (name, sch, exp, found))

        connection.commit()
        connection.close()

        return True
    except Exception as e:
        print(e)
        return False

