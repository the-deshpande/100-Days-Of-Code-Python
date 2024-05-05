from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    due_date = DateField('Due Date')
    submit = SubmitField('Add Task')
