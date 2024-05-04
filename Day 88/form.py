from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL


class AddForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[URL()])
    img_url = StringField("Image URL", validators=[URL()])
    location = StringField("Location")
    seats = StringField("Number of Seats")
    has_toilet = BooleanField("Has Toilet?")
    has_wifi = BooleanField("Has Wifi?")
    has_sockets = BooleanField("Has Sockets?")
    can_take_calls = BooleanField("Can take Calls?")
    coffee_price = StringField("Coffee Price")
    submit = SubmitField('Submit')
