import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"

def start(offset):

    querystring = {
        "offset": f"{offset}", 
        "keyword": "django", 
        "location": "helsinki"
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": token,
	    "X-RapidAPI-Host": "indeed-jobs-api-finland.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, json=headers, params=querystring)
    response.raise_for_status()

    # print(response.text)
    response = json.loads(response.text)
    print(response)
    next_page = response[0]['next_page']

    if next_page == 'True':
        offset += 10
        start(offset)
    else:
        print("No more pages")
        return


def main():
    offset = 0
    start(offset)


if __name__ == '__main__':
    main()