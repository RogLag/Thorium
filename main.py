import Spotify
import time
import os

Spotify.music()
print("The program is preparing to download the music(s), please wait...")
time.sleep(6)
Spotify.upload()
os.remove(".cache")