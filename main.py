import modules.control as control
import time




#######################################################################################################################


def album():
    
    
    '''
    This function allows you to download all the music from all the albums of the same artist from its Spotify sharing link.
    '''
    
    
    control.init()
    control.musics_albums()
    control.getLinks()
    print("The program is preparing to download the music(s), please wait...")
    time.sleep(6)
    control.download()

def music():
    
    
    '''
    This function allows you to download music from its title, artist and album (if the name of the album is much too long, unknown, it is not essential for the program, it is even advised not to enter it).
    '''
    
    
    control.init()
    control.music_artist()
    control.getLinks()
    print("The program is preparing to download the music(s), please wait...")
    time.sleep(6)
    control.download()