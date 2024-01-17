from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

API_KEY = 'TopSecretAPIKey'

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {col.name: getattr(self,col.name) for col in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random():
    random_cafe = choice(db.session.execute(db.select(Cafe)).scalars().all())
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all():
    cafes = db.session.execute(db.select(Cafe)).scalars()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])


@app.route('/search')
def get_particular():
    loc = request.args.get('loc')
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if len(cafes) == 0:
        return jsonify(error={
            'Not Found': 'Sorry no cafes found in the location'
        }), 404
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes]), 200


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def post_create():
    cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={
        'success': 'Successfully added the new cafe'
    })


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    price = int(request.args.get('price'))
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(result={
            'success': 'The data has successfully been modified'
        }), 200
    else:
        return jsonify(result={
            'failed': 'Failed to update the data, entry not found'
        }), 404


# HTTP DELETE - Delete Record
@app.route('/delete/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key = request.args.get('api_key')
    if api_key != API_KEY:
        return jsonify(error={
            'Message': 'You are not authorized, check the api_key'
        }), 403
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(result={
            'success': 'The cafe has been successfully deleted'
        }), 200
    return jsonify(error={
        'Message': 'The cafe does not exist'
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
