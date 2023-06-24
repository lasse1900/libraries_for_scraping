import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://linkedin-jobs-search.p.rapidapi.com/"

payload = {
	"search_terms": "embedded",
	"location": "Helsinki",
	"page": "1"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": token,
    "X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
response.raise_for_status()

with open('logfile_3.json', 'w', encoding='utf-8') as fp:
    json.dump(response.json(), fp, indent=2, ensure_ascii=False, sort_keys=True)