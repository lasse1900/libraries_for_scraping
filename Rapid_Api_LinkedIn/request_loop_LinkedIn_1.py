import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")


def start(offset):
    url = "https://indeed-jobs-api.p.rapidapi.com/indeed-us/"

    querystring = {"offset": f"{offset}", "keyword": "python developer", "location": "alaska"}

    headers = {
        "X-RapidAPI-Key": token,
        "X-RapidAPI-Host": "indeed-jobs-api.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

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