from pytube import YouTube

def downloader(links):
    counter = 0
    for url in links:
        counter += 1
        print("______________")
        print("Download start")
        yt = YouTube(url)
        t = yt.streams.filter(only_audio=True)
        t[0].download("G:/Mon Drive/NSI Project/Musics")
        print(f"Download finish ({counter}/{len(links)})")
    print("______________")
    print(f"Download successfully ({counter}/{len(links)}) !")
    print("\n")
    return True