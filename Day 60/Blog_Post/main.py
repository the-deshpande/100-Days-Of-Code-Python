from flask import Flask, render_template, request
from smtplib import SMTP
import requests
from dotenv import dotenv_values

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
env = dotenv_values()
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        body = (f"Subject:You are being contacted!!!\n\n"
                f"Name: {request.form['name']}\n"
                f"Email: {request.form['email']}\n"
                f"Mobile: {request.form['phone']}\n"
                f"Message: {request.form['message']}")
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=env['SENDER_EMAIL'], password=env['SENDER_PASSWORD'])
            connection.sendmail(from_addr=env['SENDER_EMAIL'], to_addrs=env['RECEIVER_EMAIL'], msg=body)

        return render_template('contact.html', submitted='Your form has been successfully submitted')
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
