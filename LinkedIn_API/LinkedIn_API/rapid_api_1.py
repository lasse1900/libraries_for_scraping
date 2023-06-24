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

with open('logfile_1.json', 'w') as fp:
    json.dump(response, fp)

print(response.text)