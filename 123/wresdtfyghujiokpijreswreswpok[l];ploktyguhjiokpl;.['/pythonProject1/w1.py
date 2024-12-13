from flask import Flask, render_template, request, flash
import random, sqlite3

app = Flask(__name__)
app.secret_key='1234'

con = sqlite3.connect('regestratiom.db', check_same_thread=False)
cursor = con.cursor()

@app.route('/authorization/', methods=['POST', 'GET'])
def auyhortization():
    if request.method == 'POST':
        login = request.form['username']
        if login == 'login':
            flash('Вы авторозованны', 'success')
            return render_template('authorization.html')
        else:
            flash('Неверный логин и пароль', 'danger')
            return render_template('login.html')
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
                       (last_name, name, patronemic, username, email, gender,password))
            con.commit()
            return f'Регистрация прошла успешно'
        else:
            return 'Ошибка пароля'

app.run(debug=True)