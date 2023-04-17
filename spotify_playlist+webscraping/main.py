from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

pp = pprint.PrettyPrinter()

URL = "https://www.billboard.com/charts/hot-100/"

SPOTIPY_CLIENT_ID = "" # your client id
SPOTIPY_CLIENT_SECRET = "" # your client secret
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

# Authenticate with Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# List of song names
music_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

response = requests.get(f"{URL}/{music_date}/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
all_songs = soup.select(selector="li h3", class_="c-title")

songs_list = [song.get_text().strip() for song in all_songs]  # strip() method removes truncates
# del songs_list[100: 110: 1] # delete the last items on the list using slicing
# or
songs_list = songs_list[:100]  # slice list to show the first 100 index

# print(len(songs_list))
print(songs_list)

# Search for each song and retrieve Spotify URIs
song_uris = []
year = music_date.split("-")[0]
# add this to track to add the year as search variable -> q=f"track:{song_name} year{year}"
for song_name in songs_list:
    result = sp.search(q=f"track:{song_name}", type="track", limit=1)
    # pp.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        # pp.pprint(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")

# Create a new private playlist with the name "YYYY-MM-DD Billboard 100" and get the playlist ID
my_playlist = sp.user_playlist_create(user=f"{user_id}", name=f"{music_date} Billboard Top 100 Tracks", public=False,
                                      description=f"Top 100 tracks in this date({music_date}) according to Billboard")
playlist_id = my_playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)



