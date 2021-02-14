import requests
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Unlike the Spotify API we only need the Access token (Key)
GENIUS_KEY =  os.getenv('GENIUS_KEY')

# We get the lyrics by passing in the song name and artist name.
def get_lyrics(song_name, artist_name):
    
    # We use the search API
    URL = 'https://api.genius.com/search'
    
    headers = {'Authorization': 'Bearer ' + GENIUS_KEY}
    
    data = {'q': song_name + ' ' + artist_name}
    
    response = requests.get(URL, data=data, headers=headers)
    
    response = response.json()
    
    # Set these equal to None if no lyrics are found.
    remote_song_info = None
    lyric_url = None
    
    for i in response['response']['hits']:
        if artist_name.lower() in i['result']['primary_artist']['name'].lower():
            remote_song_info = i
            break
    
    if remote_song_info:
        lyric_url = remote_song_info['result']['url']
        
    return lyric_url