import requests
from youtube_search import YoutubeSearch
import json
import yt_dlp
from functions_file import finditem, youtube_to_mp3, generate_playlist

# generated using : https://curlconverter.com/ to convert
# https://developer.spotify.com/documentation/web-api/reference/get-playlist curl request


# getting an access token from spotify
# how to get a client_id and client_secret:
# GO TO: https://developer.spotify.com/dashboard
# create an 'app' and reveal the ID's by navigating to the 'Settings'
data = {
    'grant_type': 'client_credentials',
    'client_id': 'ENTER YOUR ID',
    'client_secret': 'ENTER YOUR SECRET ID',
}

response1 = requests.post('https://accounts.spotify.com/api/token', data=data)

#print(response1.json())
token = response1.json()['access_token']

headers = {
    'Authorization': f'Bearer {token}',
}

params = {
    # no need to fill
}

# input playlist link
link = str(input("enter spotify playlist link: ")).split("/")[4].split("?")[0]
response = requests.get(f'https://api.spotify.com/v1/playlists/{link}', params=params, headers=headers)


jsonR = response.json()
#print(jsonR)
file = open("list.txt", "w+")


for data in jsonR["tracks"]["items"]:
    track = finditem(data, "name")
    artist = data['track']['album']['artists'][0]['name']

    results = YoutubeSearch(track + " " + artist, max_results=1).to_json()

    print(track + " " + artist)
    results = json.loads(results)

    # Accessing url_suffix for each video
    for video in results['videos']:
        if video['url_suffix'].__contains__("shorts"):
            print("Can't find it!")
        else:
            youtube_url = f"https://www.youtube.com{video['url_suffix']}"
            print(f"Found video URL: {youtube_url}")
            file.write(youtube_url + "\n")
            youtube_to_mp3(youtube_url)  # Convert to MP3

#A link to a YouTube playlist containing all the songs from the spotify playlist.
file.seek(0)
print("\n\n\n")
print("YouTube Playlist Link: ")
print(generate_playlist(file.read()))

file.close()