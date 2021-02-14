import requests
import os
import random
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

AUTH_URL = 'https://accounts.spotify.com/api/token'

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET =  os.getenv('CLIENT_SECRET')

# This method aquires the credential token from the Client ID and Secret
def get_token():
    
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
    
    return access_token

# get_info calls get_token and makes the API call with the artist ID provided
def get_info(artist_id):
    
    access_token = get_token()
    
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)
    }

    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_id)

    data = requests.get(URL + "?market=US", headers = headers)

    data = data.json()

    # We chose a random song from the artist's top tracks
    rand = random.randint(0, len(data['tracks']) - 1)
    
    song_name = data['tracks'][rand]['name']
    artist_name = data['tracks'][rand]['artists'][0]['name']
    song_img = data['tracks'][rand]['album']['images'][0]['url']
    song_preview = data['tracks'][rand]['preview_url']
    spotify_url = data['tracks'][rand]['external_urls']['spotify']
    
    info = [song_name, artist_name, song_img, song_preview, spotify_url]
    
    # Returns a list containing all the info.
    return info