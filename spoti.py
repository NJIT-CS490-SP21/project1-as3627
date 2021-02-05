import requests
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

AUTH_URL = 'https://accounts.spotify.com/api/token'

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET =  os.getenv('CLIENT_SECRET')

# artist_id = '5qEtLvXzYdv0G7c7rR6irX'

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


def get_info(artist_id):
    
    access_token = get_token()
    
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)
    }

    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_id)

    data = requests.get(URL + "?market=US", headers = headers)

    data = data.json()


    song_name = data['tracks'][0]['name']
    artist_name = data['tracks'][0]['artists'][0]['name']
    song_img = data['tracks'][0]['album']['images'][0]['url']
    song_preview = data['tracks'][0]['preview_url']

    info = [song_name, artist_name, song_img, song_preview]
    
    return info