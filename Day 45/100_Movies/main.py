import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')
movies = [movie.text+"\n" for movie in soup.select('h3.listicleItem_listicle-item__title__BfenH')]
movies.reverse()

with open('top_100_movies.txt', 'w') as file:
    file.write(''.join(movies))
