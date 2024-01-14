from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from sql import db, Movie
from form import UpdateForm, AddForm
from dotenv import dotenv_values
import requests

env = dotenv_values()

headers = {
    'Content-type': 'application-json',
    'Authorization': f'Bearer {env["TMDB_KEY"]}'
}
search_url = 'https://api.themoviedb.org/3/search/movie'
movie_url = 'https://api.themoviedb.org/3/movie/'

app = Flask(__name__)
app.config['SECRET_KEY'] = env['SQL_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)
Bootstrap5(app)

with app.app_context():
    db.create_all()

# with app.app_context():
#     new_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family ("
#                     "Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each "
#                     "other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for index, movie in enumerate(movies):
        movie.ranking = len(movies)-index
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route('/edit/<int:movie_id>', methods=['POST', 'GET'])
def edit(movie_id):
    form = UpdateForm()
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if form.validate_on_submit():
        movie.review = form.review.data
        movie.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        params = {
            'query': form.title.data
        }
        response = requests.get(search_url, headers=headers, params=params).json()
        return render_template('select.html', movie_list=response['results'])
    return render_template('add.html', form=form)


@app.route('/select/<int:movie_id>')
def select(movie_id):
    response = requests.get(f"{movie_url}/{movie_id}", headers=headers).json()
    movie = Movie(
        title=response['title'],
        year=int(response['release_date'][:4]),
        description=response['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
    )
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('edit', movie_id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
