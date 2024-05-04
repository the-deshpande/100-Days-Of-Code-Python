from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from cafe import db, Cafe
from form import AddForm
from dotenv import dotenv_values

env = dotenv_values()

app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = env['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = env['SQL_URI']
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def homepage():
    list_of_cafes = [cafe.to_dict() for cafe in db.session.execute(db.select(Cafe)).scalars()]
    return render_template('index.html', page='home', cafes=list_of_cafes)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            seats=form.seats.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            has_sockets=form.has_sockets.data,
            can_take_calls=form.can_take_calls.data,
            coffee_price=form.coffee_price.data
        )
        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('add.html', page='add', form=form)


@app.route('/cafe/<int:_id>')
def cafes(_id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == _id)).scalar()
    return render_template('cafe.html', page='cafes', cafe=cafe.to_dict())


@app.route('/delete/<int:_id>')
def delete(_id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == _id)).scalar()
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)
