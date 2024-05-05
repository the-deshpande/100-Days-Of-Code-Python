from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(500), nullable=False)
    due_date = db.Column(db.DateTime)
    finished = db.Column(db.Boolean, default=False)
    finish_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }
