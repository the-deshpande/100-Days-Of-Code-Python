from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        return f"<h1>Name: {request.form['username']}, Password: {request.form['password']}</h1>"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
