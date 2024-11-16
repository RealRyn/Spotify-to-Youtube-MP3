# **Spotify-to-Youtube-MP3**

Effortlessly convert Spotify playlists into downloadable `.mp3` files and manage YouTube links with added features for convenience. 🎵🎥

![Version](https://img.shields.io/badge/Version-1.1-brightgreen)  
![License](https://img.shields.io/github/license/RealRyn/Spotify-to-Youtube-MP3)  
![Issues](https://img.shields.io/github/issues/RealRyn/Spotify-to-Youtube-MP3)

---

## **Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Getting an Access Token from Spotify](#getting-an-access-token-from-spotify)
- [Update 1.1 Details](#update-11-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## **Features**
- Convert Spotify playlists to `.mp3` files.
- Generate a `list.txt` file containing YouTube links for the tracks.
- **New (v1.1)**: Auto-create a YouTube playlist from the tracks.
- Increased stability with improved file readability and additional notes.
- Easy-to-follow setup with `requirements.txt` for package installation.

---

## **Installation**
1. Clone the repository:
    ```bash
    git clone https://github.com/RealRyn/Spotify-to-Youtube-MP3.git
    cd Spotify-to-Youtube-MP3
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## **Usage**
1. Run the script:
    ```bash
    python main.py
    ```
2. Input the Spotify playlist link:
    - Go to your Spotify playlist → Menu → Share → Copy link to playlist.
3. `.mp3` files will be downloaded to the repository folder.
4. A `list.txt` file containing the YouTube links for the tracks will also be generated.
5. Enjoy your playlist anywhere! 🎶

---

## **Screenshots**
### Example Output:
reserved.

---

## **Getting an Access Token from Spotify**
To get started, you'll need a **client ID** and **client secret** from Spotify:
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Log in and create a new "App."
3. Navigate to the app's **Settings** and reveal your **Client ID** and **Client Secret**.

Add them to your script:
```python
data = {
    'grant_type': 'client_credentials',
    'client_id': 'ENTER YOUR ID',
    'client_secret': 'ENTER YOUR SECRET ID',
}
