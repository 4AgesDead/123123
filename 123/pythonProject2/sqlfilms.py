from asyncore import write
from doctest import debug

from flask import Flask, render_template
import json, random, sqlite3


with open('candidates.json', 'r', encoding='utf-8') as file:
    list_candidates = json.loads(file.read())
app = Flask(__name__)


def main():
    con = sqlite3.connect('ЗАДАНИЕ 5.db', check_same_thread=False)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM movies")
    main = []
    for film in cursor:
        main.append(
            {'name': film[0],
             'rating': film[1],
             'year': film[2],
             'director': film[3],
             'genre': film[4]
             }
        )
    return main

def director_search(x):
    con = sqlite3.connect('ЗАДАНИЕ 5.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM movies WHERE Режиссер = (?)", (x,))
    main = []
    for film in cursor:
        main.append(
            {'name': film[0],
             'rating': film[1],
             'year': film[2],
             'director': film[3],
             'genre': film[4]
             }
        )

    return main

def genre_search(x):
    con = sqlite3.connect('ЗАДАНИЕ 5.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM movies WHERE Жанр = (?)", (x,))
    main = []
    for film in cursor:
        main.append(
            {'name': film[0],
             'rating': film[1],
             'year': film[2],
             'director': film[3],
             'genre': film[4]
             }
        )

    return main

def year_search(y,x,z):
    con = sqlite3.connect('ЗАДАНИЕ 5.db')
    cursor = con.cursor()
    main= []
    if y == '>':
        cursor.execute("SELECT * FROM movies WHERE Год > (?)", (x,))
        for film in cursor:
            main.append(
                {'name': film[0],
                 'rating': film[1],
                 'year': film[2],
                 'director': film[3],
                 'genre': film[4]
                 }
            )
    elif y == '<':
        cursor.execute("SELECT * FROM movies WHERE Год < (?)", (x,))
        for film in cursor:
            main.append(
                {'name': film[0],
                 'rating': film[1],
                 'year': film[2],
                 'director': film[3],
                 'genre': film[4]
                 }
            )
    elif y =='><':
        cursor.execute("SELECT * FROM movies WHERE Год > (?) and Год < (?)", (x,z))
        for film in cursor:
               main.append(
                   {'name': film[0],
                    'rating': film[1],
                    'year': film[2],
                    'director': film[3],
                    'genre': film[4]
                    }
               )
    return main

def rating_search(y,x,z):
    con = sqlite3.connect('ЗАДАНИЕ 5.db')
    cursor = con.cursor()
    main= []
    if y == '>':
        cursor.execute("SELECT * FROM movies WHERE Рейтинг > (?)", (x,))
        for film in cursor:
            main.append(
                {'name': film[0],
                 'rating': film[1],
                 'year': film[2],
                 'director': film[3],
                 'genre': film[4]
                 }
            )
    elif y == '<':
        cursor.execute("SELECT * FROM movies WHERE Рейтинг < (?)", (x,))
        for film in cursor:
            main.append(
                {'name': film[0],
                 'rating': film[1],
                 'year': film[2],
                 'director': film[3],
                 'genre': film[4]
                 }
            )
    elif y =='><':
        cursor.execute("SELECT * FROM movies WHERE Рейтинг > (?) and Год < (?)", (x,z))
        for film in cursor:
               main.append(
                   {'name': film[0],
                    'rating': film[1],
                    'year': film[2],
                    'director': film[3],
                    'genre': film[4]
                    }
               )
    return main

def get_new_film(x,y,z,a,f):
    main={'name': x,
         'rating': y,
         'year': z,
         'director':a,
         'genre': f
         }
    con = sqlite3.connect('ЗАДАНИЕ 5.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO movies (Название, Рейтинг, Год, Режиссер, Жанр) VALUES (?,?,?,?,?)', (x,y,z,a,f))
    return main

@app.route('/')
def page_index():
    return render_template('sqlmain.html', films=main())


@app.route('/year/<atype>/<int:year1>/<int:year2>')
def years(atype,year1,year2):
    return render_template('sqlmain.html', films=year_search(atype,year1,year2))


@app.route('/director/<director>')
def directors(director):
    return render_template('sqlmain.html', films=director_search(director))

@app.route('/genre/<genre>')
def genres(genre):
    return render_template('sqlmain.html', films=genre_search(genre))


@app.route('/rating/<atype>/<int:rating1>/<int:rating2>')
def ratings(atype,rating1,rating2):
    return render_template('sqlmain.html', films=rating_search(atype,rating1,rating2))

@app.route('/get_new/<name>/<int:rating>/<int:year>/<director>/<genre>')
def get_new(name,rating,year,director,genre):
    return render_template('sqlmain.html', films=get_new_film(name,rating,year,director,genre))




app.run(debug=True)
