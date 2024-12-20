from flask import Flask, render_template, request, flash, url_for, redirect, session
import random, sqlite3
from flask_session import Session
from cachelib import FileSystemCache
from datetime import timedelta

app = Flask(__name__)
app.secret_key = '21561349'
app.config['SESSION_TYPE'] = 'cachelib'
app.config['SESSION_CACHELIB'] = FileSystemCache(cache_dir='flask_session', threshold=500)
Session(app)

con = sqlite3.connect('info.db', check_same_thread=False)
cursor = con.cursor()

def all():
    cursor.execute("SELECT * FROM posts")
    main = []
    for i in cursor:
        main.append(
            {'id' : i[0],
             'title': i[1],
             'image': i[2],
             'description': i[3],
             'user_name': user_name(i[4])
             }
        )
    return main

def post(id_):
    cursor.execute("SELECT * FROM posts where id = (?)", [id_])
    main = []
    data = cursor.fetchall()[0]
    main.append(
        {'id' : data[0],
         'title': data[1],
         'image': data[2],
         'description': data[3],
         'user_name': user_name(data[4])
         }
    )
    return main
def user_name(id_):
    cursor.execute("SELECT * FROM reg where id = (?)", [id_])
    return cursor.fetchall()[0][2]

@app.route('/add/')
def adds():
    if 'login' not in session:
        flash('Необходимо авторизоваться', 'danger')
        return redirect(url_for('all_in'))
    return render_template('add.html')

@app.route('/upload/', methods=['POST'])
def save_post():
    image = request.files.get('image')
    title = request.form['title']
    description = request.form['description']
    image.save(f'static/uploads/{image.filename}')
    cursor.execute('INSERT INTO posts (title, file_name, description,user_id) VALUES (?,?,?,?)',
                   (title,f'static/uploads/{image.filename}',description,session['id']))
    con.commit()
    return 'ok'
@app.route('/')
def all_in():
    return render_template('all.html', dickies=all())

@app.route('/authorization/', methods=['POST', 'GET'])
def auyhortization():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM reg")
        for i in cursor:
            print(login, i[6])
            if login == i[6] and password == i[7]:
                session['login'] = True
                session['username'] = login
                session['id'] = i[0]
                session.permanent = False
                app.permanent_session_lifetime = timedelta(minutes=1)
                session.modified = True
                flash('Вы авторозованны', 'success')
                return redirect(url_for('all_in'))
            else:
                flash('Неверный логин или пароль', 'danger')
                return redirect(url_for('gay'))
    return render_template('authorization.html')

@app.route('/login/', methods=['POST', 'GET'])
def gay():
    return render_template('login.html')

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/save_register/', methods=['POST', 'GET'])
def save_reg():
    if request.method == 'POST':
        last_name = request.form['last_name']
        name = request.form['name']
        patronemic = request.form['patronymic']
        username = request.form['username']
        email = request.form['email']
        gender = request.form['gender']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            cursor.execute('INSERT INTO reg (last_name, name, patronymic, gender, email, username, password) VALUES (?,?,?,?,?,?,?)',
                       (last_name, name, patronemic, gender, email, username,password))
            con.commit()
            return f'Регистрация прошла успешно'
        else:
            return 'Ошибка пароля'
@app.route('/logout/')
def logout():
    session.clear()
    flash('Вы вышли из профиля', 'danger')
    return redirect(url_for('all_in'))


@app.route('/posts/<int:id_>')
def ghfjh(id_):
    print(post(id_))
    return render_template('post.html', poste=post(id_)[0])
app.run(debug=True)