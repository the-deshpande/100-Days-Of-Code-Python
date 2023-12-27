import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values
import requests
from bs4 import BeautifulSoup

env = dotenv_values()

date = input('Which day do you want to time travel to ("YYYY-MM-DD") : ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')

soup = BeautifulSoup(response.text, 'html.parser')
songs = [name.text.strip()+"\n" for name in soup.select('li.o-chart-results-list__item h3#title-of-a-story')]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=env['CLIENT_ID'],
        client_secret=env['CLIENT_SECRET'],
        show_dialog=True,
        cache_path="token.txt",
        username=env['USERNAME'],
    )
)

results = [sp.search(song+date[:4], limit=1)['tracks']['items'][0]['uri'] for song in songs]
print(results)

playlist = sp.user_playlist_create(env['USERNAME'], name=date+' Billboard 100',public=False)
sp.playlist_add_items(playlist['uri'], results)
print(playlist['uri'])
