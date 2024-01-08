from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guess/<name>')
def prediction(name: str):
    response = requests.get('https://api.agify.io', params={'name': name})
    age = response.json()['age']

    response = requests.get('https://api.genderize.io', params={'name': name})
    gender = response.json()['gender']
    return render_template('prediction.html', name=name, age=age, gender=gender)


@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    return render_template('blog.html', posts=response.json())


if __name__ == '__main__':
    app.run(debug=True)
