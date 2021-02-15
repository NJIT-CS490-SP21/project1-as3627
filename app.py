import os
import random
from flask import Flask, render_template
from spoti import get_info
from genius import get_lyrics


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')

def hello_world():
    """ Returns root endpoint HTML """
    
    # These can be swapped out for any artist URI.
    # The ones in this list are (in order): Arianna Grande, Dua Lipa, Sia, The Weeknd, Bruno Mars
    ids = ['66CXWjxzNUsdJxJ2JdwvnR', '6M2wZ9GZgrQXHCFfjv46we', '5WUlDfRSoLAfcVSX1WnrxN', '1Xyo4u8uXC1ZmMpatF05PJ', '0du5cEVh5yTK9QJze8zA0C']

    idx = random.randint(0, len(ids) - 1)

    # Pass the random index through to get info for a randomly chosen artist. 
    info = get_info(ids[idx])
    
    lyrics = get_lyrics(info[0], info[1][0])
    total_artists = len(info[1])
    
    # Pass every variable we need to the front end.
    return render_template(
        "index.html",
       song_name=info[0],
       artist_name=info[1],
       total_artists=total_artists,
       song_img=info[2],
       song_preview=info[3],
       spotify_url=info[4],
       lyrics_link = lyrics,
    )
    
# Runs the app
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
