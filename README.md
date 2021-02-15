# Project 1

## Purpose / Objective
In this project, we'll deploy a simple “music discovery” web app that shows song(s) from your favorite artist(s) and link(s) to the music and lyrics.

This data will be dynamically generated using third-party APIs from Spotify and Genius.

## Steps to Deploy

### Clone the repository
1. On `https://github.com/new`, create a new personal repository. Name it whatever you want.
2. In terminal, in your home directory, clone the repo: `https://github.com/NJIT-CS490-SP21/project1-as3627.git`.
3. `cd` into the repository that is created and you should see all the files.
4. Then, connect this cloned repo to your new personal repo made in Step 1: `git remote set-url origin https://www.github.com/{your-username}/{repo-name}` (be sure to change your username and repo-name and remove the curly braces)
5. Run `git push origin main` to push the local repo to remote. You should now see this same code in your personal repo.

### Sign up for a Spotify Developer Account
1. You can sign up for a free Spotify Developer account on their website here: [https://developer.spotify.com/](https://developer.spotify.com/).
2. Once you make an account, head on over to the Dashboard and hit `Create an App`. Fill out the information on there.
3. After you finish filling in the information for creating the app, make note of the `Client ID` and `Client Secret`, we'll need them later.
4. Spotify is used to gather song data.

### Sign up for a Genius API Account
1. You can sign up for a free Genius account on this link here: [https://genius.com/signup_or_login](https://genius.com/signup_or_login).
2. Once you make an account, head over to [https://genius.com/api-clients](https://genius.com/api-clients) and hit `New API  Client` and fill in the information.
3. Once you fill in the information hit `Generate Access Token` and make note of this Access Token, we'll need it later.
4. Genius is used to gather song lyrics.

### Sign up for a Heroku Account
1. You can sign up for a free Heroku account on their website here: [https://signup.heroku.com/login](https://signup.heroku.com/login).
2. Heroku is used to host the web app.

### Install Requirements (if you don't already have them)
Note: if for some reason these commands don't work, put `sudo` in front of each command and then try running it.
1. `pip install python-dotenv`
2. `pip install requests`
3. `pip install Flask`
4. `npm install -g heroku` (Note this one might take a while to install, don't worry)

### Setup
1. Create a `.env` file in your project directory.
2. Add the Spotify `Client ID` and `Client Secret` variables inside the `.env` file, with the lines: `export CLIENT_ID = '{YOUR_ID}'` and `export CLIENT_SECRET = '{YOUR_SECRET}'`.
3. Add the Genius `Access Token` variable in the `.env` file, with the lines: `export GENIUS_KEY = '{YOUR KEY}'`.
4. Inside `app.py` add your favorite artists' Artist IDs inside the `ids` list beginning on line 18. To find out how to get Artist IDs, check this link out: 
[https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID](https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID)

### Running the Application
1. Run command in terminal with `python app.py`
2. Preview the web page in browser `'/'`

### Deploy to Heroku
1. If you don't have this file already, create `Procfile` and write `web: python app.py` on the first line. This is used to deploy the app on Heroku. 
2. If you don't have this file already, create `requirements.txt` and write `Flask`, `requests`, and `python-dotenv`. Make sure each is separated with a newline. If you use more packages, make sure to include them here.
3. Make sure to have all your files commited with git by this point.
4. Login to your Heroku account with `heroku login -i`. 
5. Create a Heroku app with the command: `heroku create`. This will create a new URL and associated host for you.
6. Push your code to Heroku with the command: `git push heroku main`. This pushes your code to Heroku's remote repository.
7. Once that's done, visit [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps). Click on the app that you made, and then hit settings. Inside settings, click on `Reveal Config Vars`.
8. Add all three variables that you had in the `.env` file: `CLIENT_ID`, `CLIENT_SECRET`, and `GENIUS_KEY` and the associated key. (Note you don't need to include quotation marks with the keys)
9. Run `heroku open` or refresh the URL if you have it open, and the web app should be running.


## Technical Issues Faced:
1. Initially with the Spotify API, there were some songs that did not have any preview. In these cases I would still be attempting to put something into the audio player, which would be giving me errors. I actually thought it was an audio player error in the beginning,
which made me go to [w3schools.com/html/html5_audio.asp](w3schools.com/html/html5_audio.asp) to check how audio players worked again. After seeing I didn't make any mistakes with the audio player, I went
back to the `json` in the python file. After running the code a few times, I found that for these songs, had `None` for their preivew url. I realized I was passing the value of `None` instead of a URL,
so I modified my HTML with Flask python tags `{% if song_preview == None %}`. Now in my code, I made it so that the audio player only comes up if a song preview link was provided.
2. Some songs had multiple artists. Initially I was pulling only the first artist of the song, since I didn't really know how to get the rest. After going through the lecture 4 demo again,
I decided to change how the code worked. Since for that demo, we passed a list and the length of the list, I decided to do the same for the artist names. Before I could do anything, I went back to the Spotify api.
I had to look back at the `json` and see where the artist names were being stored again. After I found that, I made a loop in the spotify file,
and then appended every artist name into a list. After that I also took the length of the list and returned both the list and length with the rest of the variables. 
3. When I used the Genius API, there were some cases where I could not return a lyrics page. For some reason, it would be throwing an error for me and not returning `None`, as the case
was for the Spotify API when there wasn't a song preview. I thought I was messing up with my usage of the API, so I decided to look up a tutorial on how to use the Genius API. I actually found
a link to help: [https://dev.to/willamesoares/how-to-integrate-spotify-and-genius-api-to-easily-crawl-song-lyrics-with-python-4o62](https://dev.to/willamesoares/how-to-integrate-spotify-and-genius-api-to-easily-crawl-song-lyrics-with-python-4o62)
which actually goes over a similar project. In this project's case, I followed along with the code structure and I noticed that they initially set the link to be `None`, and if there was a lyric page found, 
they would set the varible to the link. In the cases where no link was found, it would automatically return `None`. Which ended up solving my issue. This site also helped me clean up my code for API usage.


## Current Known (or Potential) Issues:
1. If the api crashes, or hit its limit for the day, the app will most likely return an error message or crash. This issue has not occured (yet), but is possible. If this occurs, I advise waiting some time before using the app again. I have not been able to fix this potential issue yet.

## Additional Features I'd like to Implement:
1. If I had more time to work on it, I would like to add a search bar so the user can search for an artist themselves. Similar to how we did HW8, I would be using Javascript with 
`@app.route("/search/<user_text>")` in Flask. I would most likely use an html button along with a text box to send the arguments to the back end. I would then create a new method under the search route, 
and make use of the Spotify Search API for searching the inputted artist's URI, and then using the top-tracks API to pick a random song. The only issue is that I had a hard time working with the JS part, especially with parsing the `json` and changing the html. 
It would take me a long time to add this feature, and givin the due date is soon, I decided against adding it. If given more time I would have implemented it.


## Extra Features I Implemented:
1. I got tired of having to hit `CTRL + R` every time to refresh the page, so I created a refresh button on the page itself. I looked up how to make a refresh button in html and 
found this site: [https://www.htmlgoodies.com/tutorials/getting_started/article.php/3479551/reloading-the-page.htm](https://www.htmlgoodies.com/tutorials/getting_started/article.php/3479551/reloading-the-page.htm)
that taught me how to do it. Clicking on the 🔄 emoji will refresh the page.
2. I added a `Play on Spotify!` feature as well. With the API's `json` it also returned a link for the song itself on Spotify. I thought it would be a good idea to include this link so the 
user can play the song right away on their Spotify. 