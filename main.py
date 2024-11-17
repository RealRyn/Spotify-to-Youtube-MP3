import requests
from youtube_search import YoutubeSearch
import json
from functions_file import finditem, youtube_to_mp3, generate_playlist


# Spotify API credentials setup (client_id and client_secret)
def get_spotify_token(client_id, client_secret):
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    api_response = requests.post('https://accounts.spotify.com/api/token', data=data)
    token = api_response.json()['access_token']
    return token


# Get playlist details from Spotify API
def get_spotify_playlist_details(token, playlist_id):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers=headers)
    return response.json()


# Search for a YouTube video based on track name and artist
def search_youtube_video(track, artist):
    results = YoutubeSearch(f"{track} {artist}", max_results=1).to_json()
    results = json.loads(results)
    return results


# Process the playlist and convert YouTube videos to MP3
def process_playlist(response_json, file):
    for data in response_json["tracks"]["items"]:
        track = finditem(data, "name")
        artist = data['track']['album']['artists'][0]['name']

        # Search for the track on YouTube
        results = search_youtube_video(track, artist)
        print(f"Downloading:    {track} {artist}")

        # Extract video URL from YouTube search results
        for video in results['videos']:
            if "shorts" in video['url_suffix']:
                print("Can't find it!")
            else:
                youtube_url = f"https://www.youtube.com{video['url_suffix']}"
                print(f"Found video URL: {youtube_url}")
                file.write(youtube_url + "\n")
                youtube_to_mp3(youtube_url)  # Convert to MP3


# Main function
def main():
    client_id = 'ENTER YOUR ID'  # Replace with your Spotify client_id
    client_secret = 'ENTER YOUR SECRET ID'  # Replace with your Spotify client_secret

    # Get Spotify access token
    token = get_spotify_token(client_id, client_secret)

    # Input Spotify playlist link
    link = input("Enter Spotify playlist link: ").split("/")[4].split("?")[0]

    # Get playlist details from Spotify
    response_json = get_spotify_playlist_details(token, link)

    # Open a file to write YouTube URLs
    file = open("list.txt", "w+")

    # Process the playlist and download videos
    process_playlist(response_json, file)

    # Generate and print YouTube playlist link
    file.seek(0)
    print("\n\n\nYouTube Playlist Link:")
    print(generate_playlist(file.read()))

    # Close the file after use
    file.close()


main()
