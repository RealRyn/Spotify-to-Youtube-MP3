Usage:
download as repo
run main.py
input spotify playlist link (playlist -> menu -> share -> copy link to playlist)
mp3 files will be downloaded to the repo folder
Enjoy!


# getting an access token from spotify
# how to get a client_id and client_secret:
# GO TO: https://developer.spotify.com/dashboard
# create an 'app' and reveal the ID's by navigating to the 'Settings'


data = {
    'grant_type': 'client_credentials',
    'client_id': 'ENTER YOUR ID',
    'client_secret': 'ENTER YOUR SECRET ID',
}



