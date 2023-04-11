import requests
import os
import json
from dotenv import load_dotenv
import time
import sys, getopt

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"
job_data = []

# filename = input("Give filename where you want to save search data (JSON): ")
# keyword = input("Give keyword you are searching: ")
# location = input("Give location: ")
# print(f"filename: {filename}, keyword: {keyword}, location: {location}")

def start(offset, filename,keyword, location):
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
		time.sleep(6)
		response = json.loads(response.text)
		next_page = response[0]['next_page']

		if next_page == 'True':
			job_data.extend(response)
			offset += 10
			start(offset, filename,keyword, location)
		else:
			job_data.extend(response)
			print("No more pages")
			json.dump(job_data, fp, indent=2, ensure_ascii=False, sort_keys=True)
			return


def main(argv):
    filename = sys.argv[1]
    keyword = sys.argv[2]
    location = sys.argv[3]
    print(filename)

    offset = 0
    start(offset, filename, keyword, location)

if __name__ == '__main__':
    main(sys.argv[1:])