from asyncore import write
from doctest import debug

from flask import Flask, render_template, request
import random, sqlite3

app = Flask(__name__)

con = sqlite3.connect('задание 1.db', check_same_thread=False)
cursor = con.cursor()



def main():
    cursor.execute("SELECT * FROM medicines")
    main = []
    for preparat in cursor:
        main.append(
            {'name': preparat[0],
             'manufacturer': preparat[1],
             'form': preparat[2],
             'price': preparat[3],
             'id': preparat[4]
             }
        )
    return main


def find(x, y):
    cursor.execute('SELECT * FROM medicines')
    main = []
    for preparat in cursor:
        if x == 'manufacturer' and preparat[1] == y:
            main.append(
                {'name': preparat[0],
                 'manufacturer': preparat[1],
                 'form': preparat[2],
                 'price': preparat[3],
                 'id': preparat[4]
                 }
            )
        elif x == 'name' and preparat[0] == y:
            main.append(
                {'name': preparat[0],
                 'manufacturer': preparat[1],
                 'form': preparat[2],
                 'price': preparat[3],
                 'id': preparat[4]
                 }
            )
        elif x == 'form' and preparat[2] == y:
            main.append(
                {'name': preparat[0],
                 'manufacturer': preparat[1],
                 'form': preparat[2],
                 'price': preparat[3],
                 'id': preparat[4]
                 }
            )
    print(main)
    return main

def nujno():
    cursor.execute("SELECT * FROM medicines")
    m = 0
    for preparat in cursor:
        m += 1
    return m

def for_the_change(x, y, z, g, r):
    main = []
    main.append(
        {'name': x,
         'manufacturer': y,
         'form': z,
         'price': g,
         'id': r
         }
    )
    return main


@app.route('/')
def page_index():
    return render_template('qwerty.html', preparates=main())


@app.route('/find/')
def find1():
    return render_template('asdf.html')


@app.route('/result_find/')
def find_page():
    type_find = request.args.get('type_find')
    text = request.args.get('search_value')
    return render_template('qwerty.html', preparates=find(type_find, text))


@app.route('/rechange/')
def rechange():
    return render_template('rechange.html')


@app.route('/change_result/')
def change():
    name = request.args.get('name')
    manufacturer = request.args.get('manufacturer')
    form = request.args.get('form')
    price = request.args.get('price')
    cursor.execute('INSERT INTO medicines (name, manufacturer, form, price, id) VALUES (?,?,?,?,?)',
                   (name, manufacturer, form, price, nujno()+1))
    con.commit()
    return render_template('qwerty.html', preparates=for_the_change(name, manufacturer, form, price, nujno()))


app.run(debug=True)
