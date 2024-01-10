from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

response = requests.get('https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw'
                        '/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json').json()
posts = sorted([Post(i) for i in response], key=lambda x: x.post_id)


@app.route('/')
def homepage():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    print(posts[post_id-1].image)
    return render_template('post.html', post=posts[post_id-1])


if __name__ == '__main__':
    app.run(debug=True)
