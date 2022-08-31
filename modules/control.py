from ast import Continue
import spotipy
import modules.spotify_module as spotify_module
import modules.youtube_module as youtube_module
import modules.downloader_module as downloader_module
import os
from spotipy.oauth2 import SpotifyClientCredentials




#######################################################################################################################


#Initialization of mandatory variables for the program that will be filled later
api_key_ytb = None
client_id = None
client_secret = None
sp = None
file = None

def init():
    
    
    '''
    This function allows the program to initialize itself for future research by asking for the API identifiers that will allow it to work, the program has no way of keeping them (the cache is deleted at each end of the program's work)
    '''
    
    
    global api_key_ytb,client_id,client_secret,sp,file
    
    #Mandatory filling of variables by the user
    api_key_ytb = input("Enter your youtube api key (obligatory) :\n")
    while api_key_ytb == "":
        api_key_ytb = input("Enter your youtube api key (obligatory) :\n")
    client_id=input("Enter your client id spotify (obligatory) :\n")
    while client_id == "":
        client_id=input("Enter your client id spotify (obligatory) :\n")
    client_secret=input("Enter your client secret spotify (obligatory) :\n")
    while client_secret == "":
        client_secret=input("Enter your client secret spotify (obligatory) :\n")
    file = input("Enter the folder link from the root of the computer (with / ) (obligatory) :\n")
    while file == "":
        file = input("Enter the folder link from the root of the computer (with / ) (obligatory) :\n")
    
    #Login to spotify api
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id,client_secret))

def musics_albums():
    
    
    '''
    This function allows you to start searching for music from all the albums of the same artist and to save them in a text file in the form of (Title Album Artist). File that is deleted at the end of the program's work.
    '''
    
    
    global sp
    
    #asks the user for the criteria of the search
    artist = input("Enter the name of the artist (obligatory) :\n")
    while artist == "":
        artist = input("Enter the name of the artist (obligatory) :\n")
    artist_id = input("Enter the spotify id of the artist (obligatory) :\n")
    while artist_id == "":
        artist_id = input("Enter the spotify id of the artist (obligatory) :\n")
    print("\n")

    #create and open the text file that saves the music found
    fichier = open("data.txt", "a")

    #Search request to another module (Spotify_Module)
    albums = spotify_module.getAlbum(artist_id,client_id,client_secret)

    #Save data to text file
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
    
    
    '''
    This function allows you to search for music saved in a text file in the form (Title Album Artist). File that is deleted when the program finishes working.
    '''
    
    
    global sp
    
    #asks the user for the criteria of the search
    music_name = input("Enter the name of the music (obligatory) :\n")
    while music_name == "":
        music_name = input("Enter the name of the music (obligatory) :\n")
    artist = input("Enter the name of the artist (obligatory) :\n")
    while artist == "":
        artist = input("Enter the name of the artist (obligatory) :\n")
    album = input("Enter the name of the album who owns the music (If you don't know the artist or to help find the song if the previous download does not match your search) :\n")
    print("\n")
    
    
    #create and open a text file to save the data entered by the user
    fichier = open("data.txt", "a")
    
    
    #save data
    chaine = ""
    chaine += f'{music_name}'
    chaine += f' {album}'
    chaine += f' {artist}'
    fichier.write(f"{chaine}\n")
    
    fichier.close()
    
    print("The music was collected !")

def getLinks():
    
    
    '''
    This function makes it possible to obtain the links of the music recorded in the file created by one of the two previous functions.
    '''
    
    #loading data from file
    fichier = open("data.txt", "r")
    names = []
    error = False
    for i in fichier:
        names.append(i)
    
    #processing of the search for links thanks to another module (Youtube_Module)
    counter = -1
    while counter != len(names)-1:
        counter += 1
        if error != True:
            error = youtube_module.search(names[counter],api_key_ytb)
            
    fichier.close()
    
    print("All links have been collected !")
    
def download():
    
    
    '''
    This function allows you to download music from the links obtained saved in the file created by the Youtube_Module module
    '''
    
    
    global file
    
    #loading data from file
    fichier = open("links.txt", "r")
    links = []
    for i in fichier:
        links.append(i)
        
    fichier.close()
    
    #Launch of the download module with the links of the music and the folder that will receive the music
    downloader_module.downloader(links,file)
    
    #Destruction of data files and cache because it is the end of the program
    try:
        os.remove(".cache")
    except FileNotFoundError:
        Continue
    os.remove("data.txt")
    os.remove("links.txt")
    
    print("All music has been downloaded !")
    
    return True