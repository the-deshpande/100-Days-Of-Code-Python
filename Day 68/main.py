from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from schema import db, User
from flask_login import login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if db.session.execute(db.select(User).where(User.email == request.form['email'])).scalar():
            flash('Account with this username already exists!')
            return render_template('register.html')

        user = User(
            name=request.form['name'],
            password=generate_password_hash(request.form['password'], 'pbkdf2:sha256', 8),
            email=request.form['email']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = db.session.execute(db.select(User).where(User.email == request.form['email'])).scalar()

        if user and check_password_hash(user.password, request.form['password']):
            if login_user(user):
                flash('Successfully Logged in')
                return redirect(url_for('secrets'))
        flash('Incorrect Credentials')
        return render_template('login.html')

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('./static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
