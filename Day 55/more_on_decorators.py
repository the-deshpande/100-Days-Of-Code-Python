from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


def make_italic(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


@app.route('/')
@make_bold
@make_italic
@make_underlined
def hello_world():
    return 'Hello World!'


@app.route("/username/<name>")
def greet(name):
    return f"Hello! {name}"


if __name__ == '__main__':
    app.run(debug=True)
