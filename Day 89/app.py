from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from form import TaskForm
from schema import Task, db
from dotenv import dotenv_values
from datetime import datetime

env = dotenv_values()

app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = env['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = env['SQL_URI']
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = TaskForm()
    if form.is_submitted():
        task = Task(
            task=form.task.data,
            due_date=form.due_date.data
        )
        db.session.add(task)
        db.session.commit()

    tasks = [task.to_dict()
             for task in db.session.execute(db.select(Task).order_by(Task.finished).order_by(Task.due_date)).scalars()]
    print(tasks)
    return render_template('index.html', form=form, tasks=tasks, today=datetime.today())


@app.route('/delete/<int:_id>')
def delete(_id: int):
    task = db.session.execute(db.select(Task).where(Task._id == _id)).scalar()
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('homepage'))


@app.route('/finish/<int:_id>')
def finish(_id: int):
    task = db.session.execute(db.select(Task).where(Task._id == _id)).scalar()
    task.finished = True
    task.finish_date = datetime.today()
    db.session.commit()

    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)
