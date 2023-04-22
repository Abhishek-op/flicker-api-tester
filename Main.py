import requests

import sys

def fetch_flicker_api():

    url = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=81e25a3a31d13ff8f7522859cf643336&user_id=198161577@N03&format=json&nojsoncallback=1"

    response = requests.get(url)

    print(response.json())

if __name__ == "__main__":

    fetch_flicker_api()
