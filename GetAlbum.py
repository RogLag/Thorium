import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def GetAlbum(ArtistID,client_id,client_secret):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id,
                                                           client_secret))
    results = spotify.artist_albums(ArtistID, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
            
    return albums