import requests
from bs4 import  BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# top 100 billboard a partir de yyyy-MM-dd

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(URL + date)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.select("li ul li h3")

#interação com spotfy

SPOTFY_CLIENT_ID = "SPOTFY_CLIENT_ID"
SPOTFY_SECRET_KEY = "SPOTFY_SECRET_KEY"

song_names = [song.getText().strip() for song in all_songs]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTFY_CLIENT_ID,
                                                           client_secret=SPOTFY_SECRET_KEY))

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
results = sp.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()





