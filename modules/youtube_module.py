from apiclient.discovery import build




#######################################################################################################################


def search(query,api_key):
    
    
    '''
    Function that makes a request to the google api to obtain youtube video links from transmitted data and saves them in a text file
    '''
    
    
    youtube = build('youtube','v3',developerKey = api_key)
    fichier = open("links.txt", "a")

    try:
        request = youtube.search().list(q=f'{query}',part='snippet',type='video',maxResults=1)
        res = request.execute()
        for item in res['items']:
            fichier.write(f"https://www.youtube.com/watch?v={item['id']['videoId']}\n")
        return False
    
    except:
        print("\nQuotaError\n")
        return True
    