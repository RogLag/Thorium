import spotipy
from spotipy.oauth2 import SpotifyClientCredentials




#######################################################################################################################


def getAlbum(ArtistID,client_id,client_secret):
    
    
    '''
    Function that makes a request to the spotify api to get all the music from all the albums of a given artist
    '''
    
    
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id,
                                                           client_secret))
    
    results = spotify.artist_albums(ArtistID, album_type='album')
    albums = results['items']
    
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
            
    return albums
