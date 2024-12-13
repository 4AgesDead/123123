import sqlite3

con = sqlite3.connect('ЗАДАНИЕ 6.db')
cursor = con.cursor()
a = [[input('1 продукт '),input('вес ')],[input('2 продукт '),input('вес ')],[input('3 продукт '),input('вес ')]]
cursor.execute("SELECT calories FROM calories WHERE name IN (?)", (a[0][0],))
print(cursor.fetchall())
