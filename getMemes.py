import requests

def getMemes():
    url = "https://meme-api.herokuapp.com/gimme"
    data = requests.get(url).json()
    if(data["nsfw"] == False):
        return data["url"]
