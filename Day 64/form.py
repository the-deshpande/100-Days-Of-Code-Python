from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class UpdateForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    update = SubmitField('Update')


class AddForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    search = SubmitField('Search')
