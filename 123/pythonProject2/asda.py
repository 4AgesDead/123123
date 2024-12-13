from asyncore import write
from doctest import debug

from flask import Flask, render_template
import json, random


with open('candidates.json', 'r', encoding='utf-8') as file:
    list_candidates = json.loads(file.read())
app  = Flask(__name__)

def index():
    candidates=[]
    for candidate in list_candidates:
        candidates.append(
            {
                'name':candidate['name'],
                'position':candidate['position'],
                'skills':candidate['skills'],
            }
        )
    return candidates


def Candidate(x):
    main= {'name':list_candidates[x]["name"],
           'position': list_candidates[x]["position"],
           'skill': list_candidates[x]["skills"],
           'img': list_candidates[x]["picture"]
    }
    return  main

def skillas(x):
    candidates=[]
    for candidate in list_candidates:
        a = candidate['skills']
        while a != '':
            th = a.find(',')
            if th>=0:
                y=a[0:th].strip()
                a=a[th+1:len(a)].strip()
                if  y.lower() == x:
                    candidates.append(
                        {
                            'name': candidate['name'],
                            'position': candidate['position'],
                            'skills': candidate['skills'],
                        }
                    )

            else:
                if a.lower() == x:
                    candidates.append(
                        {
                            'name': candidate['name'],
                            'position': candidate['position'],
                            'skills': candidate['skills'],
                        }
                    )
                break

    return candidates
@app.route('/')
def page_index():
    return render_template('main.html', users=index())

@app.route('/candidate/<int:id>')
def pages(id):
    return render_template('index.html', user=Candidate(id))

@app.route('/skills/<skill>')
def skills(skill):
    return render_template('about.html', users=skillas(skill))

app.run(debug = True)