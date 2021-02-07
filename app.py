import os
import random
from flask import Flask, render_template
from spoti import get_info



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')

def hello_world():
    """ Returns root endpoint HTML """
    
    # These are temp: but belong to Arianna Grande, Lyn (Persona 5 OST), and Hollywood Principle 
    ids = ['66CXWjxzNUsdJxJ2JdwvnR', '5qEtLvXzYdv0G7c7rR6irX', '6ldZGvFDjs6KafLouTBHJ9']

    idx = random.randint(0, len(ids) - 1)

    # Pass the random index through to get info for a randomly chosen artist. 
    info = get_info(ids[idx])
    
    return render_template(
        "index.html",
       song_name=info[0],
       artist_name=info[1],
       song_img=info[2],
       song_preview=info[3],
    )
# Runs the app
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
