import requests
import os
import json
import sys
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"
job_data = []
filename = "auto_loop4.json"
keyword = "embedded"
location = "tampere"

def start(offset, argv1, argv2, argv3, argv4):
	with open(filename, 'a+', encoding='utf-8') as fp:
		querystring = {
			"offset": f"{offset}", 
			"keyword": keyword, 
			"location": location
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
			job_data.extend(response)
			offset = +10
			start(offset)
		else:
			job_data.extend(response)
			print("No more pages")
			json.dump(job_data, fp, indent=2, ensure_ascii=False, sort_keys=True)
			return

def main(argv1, argv2, argv3, argv4):
    print(argv1, " ", argv2)
    offset = 0
    start(offset.__str__(), argv1, argv2, argv3, argv4)


if __name__ == '__main__':
    main(sys.argv[1:].__str__())