from asyncore import write
from doctest import debug

from flask import Flask
import json, random


with open('candidates.json', 'r', encoding='utf-8') as file:
    list_candidates = json.loads(file.read())
app  = Flask(__name__)
main = ''
for i in range(len(list_candidates)):
    main+= (f'<pre> <h1>{list_candidates[i]["name"]}</h1>'
            f'<h2>{list_candidates[i]["position"]}</h2>'
            f'<h2>{list_candidates[i]["skills"]}</h2></pre>')

def Candidate(x):
    img = f'<img src={list_candidates[x]["picture"]}>'
    main= (f'<pre> <h1>{list_candidates[x]["name"]}</h1>'
            f'<h2>{list_candidates[x]["position"]}</h2>'
            f'<h2>{list_candidates[x]["skills"]}</h2></pre>')
    return img+main
def skillas(x):
    main=""
    for i in range(len(list_candidates)):
        f= list_candidates[i]['skills'].find(x)
        a =' ' + list_candidates[i]['skills']
        if f>=0 and a[f-1] == ' ' :
            main += (f'<pre> <h1>{list_candidates[i]["name"]}</h1>'
                f'<h2>{list_candidates[i]["position"]}</h2>'
                f'<h2>{list_candidates[i]["skills"]}</h2></pre>')
    return main
@app.route('/')
def page_index():
    return main

@app.route('/candidate/<int:id>')
def pages(id):
    return Candidate(id)

@app.route('/skills/<skill>')
def skills(skill):
    return skillas(skill)

app.run(debug = True)