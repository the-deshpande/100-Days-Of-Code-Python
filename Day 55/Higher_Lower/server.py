from flask import Flask
from random import randint

app = Flask(__name__)
number = randint(0, 9)


def answer_decorator(func):
    def wrapper(guess: int):
        if guess == number:
            text = '<h1 style="color: green">You found me</h1>'
            url = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

        elif guess < number:
            text = '<h1 style="color: red">Too low, Try Again</h1>'
            url = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'

        else:
            text = '<h1 style="color: purple">Too high, try again</h1>'
            url = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

        return func(text, url)

    return wrapper


@app.route('/')
def homepage():
    return ('<h1>Guess a number between 0 and 9<h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"'
            'alt="Alot of numbers"/>')


@app.route('/<int:guess>')
@answer_decorator
def guessed(text: str, url: str):
    return (f"{text}"
            f"<img src={url} alt='random image i found'>")


if __name__ == '__main__':
    app.run(debug=True)
