from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

success = {
    'email': 'admin@email.com',
    'password': '12345678'
}


class MyForms(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = 'the_deshpande'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST", 'GET'])
def login():
    form = MyForms()
    if form.validate_on_submit():
        if form.email.data == success['email'] and form.password.data == success['password']:
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
