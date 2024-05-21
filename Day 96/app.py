from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import requests
from random import choice
from quiz import House, Spells
from dotenv import dotenv_values

env = dotenv_values()

app = Flask(__name__)
Bootstrap5(app)

CHARACTERS = requests.get(env.get('ALL_API')).json()
SPELLS = requests.get(env.get('SPELLS_API')).json()


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/house')
def house():
    character = choice(CHARACTERS)
    return render_template('quiz.html',
                           heading='Guess the House!',
                           question=House(character))


@app.route('/spells')
def spells():
    list_spells = []
    while len(list_spells) != 4:
        new_spell = choice(SPELLS)
        if new_spell not in list_spells:
            list_spells.append(new_spell)

    return render_template('quiz.html',
                           heading='Guess the Spell!',
                           question=Spells(list_spells))


@app.route('/correct')
def correct():
    return render_template('index.html', correct=1)


@app.route('/incorrect')
def incorrect():
    return render_template('index.html', correct=2)


if __name__ == '__main__':
    app.run(debug=True)
