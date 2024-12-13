from flask import Flask, render_template, request
import random, sqlite3

app = Flask(__name__)

con = sqlite3.connect('fsd.db', check_same_thread=False)
cursor = con.cursor()

def all():
    cursor.execute("SELECT * FROM posts")
    main = []
    for i in cursor:
        main.append(
            {'id' : i[0],
             'title': i[1],
             'image': i[2],
             'description': i[3]
             }
        )
    return main

@app.route('/')
def page_index():
    return 'hello world'

@app.route('/add/')
def adds():
    return render_template('add.html')

@app.route('/upload/', methods=['POST'])
def save_post():
    image = request.files.get('image')
    title = request.form['title']
    description = request.form['description']
    image.save(f'static/uploads/{image.filename}')
    cursor.execute('INSERT INTO posts (title, file_name, description) VALUES (?,?,?)',
                   (title,f'static/uploads/{image.filename}',description))
    con.commit()
    return 'ok'
@app.route('/all_posts/')
def all_in():
    return render_template('all.html', dickies=all())


app.run(debug=True)