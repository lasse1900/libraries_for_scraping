import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://linkedin-jobs-search.p.rapidapi.com/"

pagenumber = 1

for i in range(0, 1):

	payload = {
		"search_terms": "python",
		"location": "Helsinki",
		"page": pagenumber
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": token,
		"X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
	}

	response = requests.request("POST", url, json=payload, headers=headers)
	response.raise_for_status()

with open('logfile_4.json', 'w', encoding='utf-8') as fp:
    json.dump(response.json(), fp, indent=2, ensure_ascii=False, sort_keys=True)