from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired


class ImageForm(FlaskForm):
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg']), DataRequired()])
    num_of_colors = IntegerField('Number of Colors', default=10)
    submit = SubmitField('Find')
