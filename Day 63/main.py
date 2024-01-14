from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db.init_app(app)
all_books = []


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books = db.session.execute(db.select(Books).order_by(Books.title)).scalars()
    return render_template('index.html', books=books)


@app.route("/add", methods=["GET", 'POST'])
def add():
    if request.method == 'POST':
        book = Books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<int:book_id>', methods=['POST', 'GET'])
def edit(book_id):
    book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    if request.method == 'GET':
        return render_template('edit.html', book=book)

    book.rating = request.form['rating']
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
