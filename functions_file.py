# find key 'name' (of track) in the json dictionary recursively

def finditem(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            item = finditem(v, key)
            if item is not None:
                return item


import yt_dlp
import sys
import os


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
