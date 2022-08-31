from ast import Continue
import spotipy
import modules.spotify_module as spotify_module
import modules.youtube_module as youtube_module
import modules.downloader_module as downloader_module
import os
from spotipy.oauth2 import SpotifyClientCredentials




#######################################################################################################################

api_key_ytb = None
client_id = None
client_secret = None
sp = None
file = None

def init():
    global api_key_ytb,client_id,client_secret,sp,file
    api_key_ytb = input("Enter your youtube api key :\n")
    client_id=input("Enter your client id spotify :\n")
    client_secret=input("Enter your client secret spotify :\n")
    file = input("Enter the folder link from the root of the computer (with 3[1m / 3[0m) :\n")
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id,client_secret))

def musics_albums():
    global sp
    artist = input("Enter the name of the artist :\n")
    artist_id = input("Enter the spotify link to the artist :\n")
    print("\n")

    fichier = open("data.txt", "a")

    albums = spotify_module.GetAlbum(artist_id,client_id,client_secret)

    for Album in albums:
        if Album['artists'][0]['id'] == artist_id:
            results = sp.album_tracks(Album['id'])

            for track in results['items']:
                chaine = ""
                chaine += f'{track["name"]}'
                chaine += f' {Album["name"]}'
                chaine += f' {artist}'
                fichier.write(f"{chaine}\n")
    fichier.close()
    
    print("All music has been collected !")

def music_artist():
    global sp
    music_name = input("Enter the name of the music :\n")
    artist = input("Enter the name of the artist :\n")
    album = input("Enter the name of the album who owns the music :\n")
    print("\n")
    
    fichier = open("data.txt", "a")
    
    chaine = ""
    chaine += f'{music_name}'
    chaine += f' {album}'
    chaine += f' {artist}'
    fichier.write(f"{chaine}\n")
    fichier.close()
    
    print("The music was collected !")

def getLinks():
    fichier = open("data.txt", "r")
    names = []
    error = False
    for i in fichier:
        names.append(i)
    counter = -1
    while counter != len(names)-1:
        counter += 1
        if error != True:
            error = youtube_module.search(names[counter],api_key_ytb)
    fichier.close()
    print("All links have been collected !")
    
def download():
    global file
    fichier = open("links.txt", "r")
    links = []
    for i in fichier:
        links.append(i)
    fichier.close()
    downloader_module.downloader(links,file)
    try:
        os.remove(".cache")
    except FileNotFoundError:
        Continue
    os.remove("data.txt")
    os.remove("links.txt")
    print("All music has been downloaded !")
    return True