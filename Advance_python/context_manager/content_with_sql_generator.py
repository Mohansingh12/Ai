from contextlib import contextmanager
import sqlite3


@contextmanager
def new_con(database_name:str, data_):
    try:
        with sqlite3.connect(database_name) as conn:
            cursor = conn.cursor()
            ans=cursor.execute(data_)

            yield ans
            conn.commit()
    finally:
        conn.close()
data= ''' select * from data_storage'''
with new_con('data.db',data) as F:
    print(F.fetchall())






