import sqlite3

con = sqlite3.connect('ЗАДАНИЕ 5.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM movies WHERE Рейтинг>8.5 and Год>1999")
print(cursor.fetchall())
