import sqlite3

con = sqlite3.connect('ЗАДАНИЕ 3.db')
cursor = con.cursor()
cursor.execute("SELECT form FROM medicines WHERE name='амоксициллин'")
print(cursor.fetchall())
