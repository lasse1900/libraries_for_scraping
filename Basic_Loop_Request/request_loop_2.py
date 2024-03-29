import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"

def start(offset):
	with open('auto_loop2.json', 'a+', encoding='utf-8') as fp:
		querystring = {
			"offset": f"{offset}", 
			"keyword": "embedded", 
			"location": "tampere"
		}

		headers = {
			"content-type": "application/json",
			"X-RapidAPI-Key": token,
			"X-RapidAPI-Host": "indeed-jobs-api-finland.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)
		
		print(response.text)
		response = json.loads(response.text)
		next_page = response[0]['next_page']

		if next_page == 'True':
			json.dump(response, fp, indent=2, ensure_ascii=False, sort_keys=True)
			offset += 10
			start(offset)
		else:
			json.dump(response, fp, indent=2, ensure_ascii=False, sort_keys=True)
			print("No more pages")
			return


def main():
    offset = 0
    start(offset)


if __name__ == '__main__':
    main()