import sqlite3

con = sqlite3.connect('ЗАДАНИЕ 4.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM t_shirts WHERE размер='L' and цена<100 and цвет!='красный'")
print(cursor.fetchall())
