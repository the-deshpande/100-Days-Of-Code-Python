from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
posts = sorted([Post(i) for i in response], key=lambda x: x.post_id)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    return render_template('post.html', post=posts[blog_id-1])


if __name__ == "__main__":
    app.run(debug=True)
