from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/invite')
def invite():
    return render_template('invite.html')


@app.route('/website')
def website():
    return render_template('website.html')


if __name__ == '__main__':
    app.run(debug=True)
