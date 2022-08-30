import spotipy
import GetAlbum
import search
import downloader
import time
from spotipy.oauth2 import SpotifyClientCredentials




#######################################################################################################################

api_key_ytb = None
client_id = None
client_secret = None

def start():
    global api_key_ytb,client_id,client_secret
    api_key_ytb = input("Enter your youtube api key :\n")
    client_id=input("Enter your client id spotify :\n")
    client_secret=input("Enter your client secret spotify :\n")
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id,client_secret))
    artist = input("Enter the name of the artist :\n")
    artist_id = input("Enter the spotify link to the artist :\n")
    print("\n")

    fichier = open("data.txt", "a")

    albums = GetAlbum.GetAlbum(artist_id,client_id,client_secret)

    for Album in albums:
        if Album['artists'][0]['id'] == artist_id:
            results = sp.album_tracks(Album['id'])

            for track in results['items']:
                chaine = ""
                chaine += f'{track["name"]}'
                chaine += f' {Album["name"]}'
                #chaine += f'\ncover art    : {track["album"]["images"][0]["url"]}'
                chaine += f' {artist}'
                fichier.write(f"{chaine}\n")
    fichier.close()
    print("All music has been collected !")

def link():
    fichier = open("data.txt", "r")
    names = []
    for i in fichier:
        names.append(i)
    counter = -1
    while counter != len(names)-1:
        counter += 1
        search.search(names[counter],api_key_ytb)
    print("All links have been collected !")
    fichier.close()

def upload():
    fichier = open("links.txt", "r")
    links = []
    for i in fichier:
        links.append(i)
    fichier.close()
    file = input("Enter the folder link from the root of the computer (with 3[1m / 3[0m) :\n")
    downloader.downloader(links,file)
    print("All music has been uploaded !")
    return True


def music():
    start()
    link()