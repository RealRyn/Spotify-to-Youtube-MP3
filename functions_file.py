import yt_dlp
import sys
import os


# find key 'name' (of track) in the json dictionary recursively

def finditem(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            item = finditem(v, key)
            if item is not None:
                return item


# YouTube link to mp3 file
def youtube_to_mp3(youtube_url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Downloaded and converted to MP3: {youtube_url}")

    except Exception as e:
        print(f"Error downloading {youtube_url}: {e}")


def generate_playlist(all_links):
    # Initialize an empty list to store video IDs
    array_of_ids = []

    # Split the input text into individual lines
    array_of_links = all_links.strip().split('\n')

    # Process each link
    for each_link in array_of_links:
        if '?v=' in each_link:
            split_one = each_link.split('?v=')[1]
            yt_id = split_one.split('&')[0] if '&' in split_one else split_one
        elif '.be/' in each_link:
            split_one = each_link.split('.be/')[1]
            yt_id = split_one.split('?')[0] if '?' in split_one else split_one
        else:
            yt_id = each_link  # If it doesn't match, assume it's already the ID

        array_of_ids.append(yt_id)

    # Generate the playlist link
    playlist_link = f"https://www.youtube.com/watch_videos?video_ids={','.join(array_of_ids)}"
    return playlist_link

