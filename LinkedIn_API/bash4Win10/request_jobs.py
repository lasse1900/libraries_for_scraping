import requests
import os
import json
from dotenv import load_dotenv
import time
import sys
import inspect

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"
job_data = []

def start(offset, filename, keyword, location):
	print(f"at start-> filename: {filename}, keyword: {keyword}, location: {location}")
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
		
		# print(response.text)
		time.sleep(6)
		response = json.loads(response.text)
		next_page = response[0]['next_page']

		if next_page == 'True':
			job_data.extend(response)
			offset += str(10)
			start(offset, filename,keyword, location)
		else:
			job_data.extend(response)
			print("No more pages")
			json.dump(job_data, fp, indent=2, ensure_ascii=False, sort_keys=True)
			return


def load_jobs(argv1, argv2, argv3):
    print("argumentit: ", argv1, argv2, argv3)
    
    num_args = len(inspect.signature(load_jobs).parameters)
    print(f"number of arguments: {num_args}")  # Output: 3
    
    offset = "0" # RapidAPI specific to read 10 jobs on one searchpage
    filename = argv1
    print(f'filename: {filename}')
    keyword = argv2
    print(f'keyword: {keyword}')
    print(f'{len(sys.argv)} argumet(s) were given')
    location = argv3
    print(f"{location}")
    
    if num_args == 3:
    #    location = sys.argv[3]
       print(f"location: {location} ")
       start(offset.__str__(), filename, keyword, location)
    else:
       start(offset.__str__(), filename, keyword, location='suomi')
    