import requests
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

GENIUS_KEY =  os.getenv('GENIUS_KEY')

def get_lyrics(song_name, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_KEY}
    search_url = base_url + '/search'
    data = {'q': song_name + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    
    response = response.json()
    print(response)

get_lyrics("Future Nastolgia", 'Dua Lipa')