import control
import time

def album():
    control.init()
    control.musics_albums()
    control.getLinks()
    print("The program is preparing to download the music(s), please wait...")
    time.sleep(6)
    control.download()

def music():
    control.init()
    control.music_artist()
    control.getLinks()
    print("The program is preparing to download the music(s), please wait...")
    time.sleep(6)
    control.download()
