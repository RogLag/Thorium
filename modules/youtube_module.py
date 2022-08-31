from apiclient.discovery import build

def search(query,api_key):
    youtube = build('youtube','v3',developerKey = api_key)
    fichier = open("links.txt", "a")

    #Print the title
    try:
        request = youtube.search().list(q=f'{query}',part='snippet',type='video',maxResults=1)
        res = request.execute()
        for item in res['items']:
            fichier.write(f"https://www.youtube.com/watch?v={item['id']['videoId']}\n")
        return False
    except:
        print("\nQuotaError\n")
        return True
    