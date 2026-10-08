import sqlite3
DATA=[
    [1,'harry potter'],
    [2,'lord of the rings']

]
with sqlite3.connect('data.db') as conn:
    try:
        cursor=conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS data_storage(ID INTEGER, BOOK TEXT)''')
        for id_,book in DATA:
            cursor.execute('INSERT INTO data_storage VALUES (?,?)', (id_, book))
        conn.commit()
    finally:
        conn.commit()

