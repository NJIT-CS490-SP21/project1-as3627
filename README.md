# Project 1

More information will be added to this later.


## Sign up for a Spotify Developer Account
1. You can sign up for a free Spotify Developer account on their website here: [https://developer.spotify.com/](https://developer.spotify.com/)
2. Once you make an account, head on over to the Dashboard and hit `Create an App`. Fill out the information on there.
3. After you finish filling in the information for creating the app, make note of the `Client ID` and `Client Secret`, we'll need them later.

## Sign up for a Genius API Account
1. You can sign up for a free Genius account on this link here: [https://genius.com/signup_or_login](https://genius.com/signup_or_login)
2. Once you make an account, head over to [https://genius.com/api-clients](https://genius.com/api-clients) and hit `New API  Client` and fill in the information.
3. Once you fill in the information hit `Generate Access Token` and make note of this Access Token, we'll need it later.


## Install Requirements (if you don't already have them)
Note: if for some reason these commands don't work, put `sudo` in front of each command and then try running it.
1. `pip install python-dotenv`
2. `pip install requests`
3. `pip install Flask`
4. `npm install -g heroku`

## Setup
1. Create a `.env` file in your project directory.
2. Add the Spotify `Client ID` and `Client Secret` variables inside the `.env` file, with the lines: `export CLIENT_ID = {YOUR_ID}` and `export CLIENT_SECRET = {YOUR_SECRET}`.
3. Add the Genius `Access Token` variable in the `.env` file, with the lines: `export GENIUS_KEY = {YOUR KEY}`.
4. Inside `app.py` add your favorite artist's Artist ID inside the `ids` list on line 17. To find out how to get Artist IDs, check this link out: 
[https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID](https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID)

## Running the Application
1. Run command in terminal with `python app.py`
2. Preview the web page in browser '/'

## Current Known (or Potential) Issues:
1. If the api crashes, or hit its limit for the day, I have no idea what will happen to the app itself. This error has not occured (yet). To prevent this, I will be adding in dummy data in the future that the app can use as default in the case the api call fails.
2. Some songs have multiple artists, but for those songs only 1 artist appears. This could be fixed by checking if there are multiple artists from the json and restructuring the code to pull them out. 