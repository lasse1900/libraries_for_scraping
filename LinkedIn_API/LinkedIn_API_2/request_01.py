import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("X-RapidAPI-Key")

url = "https://linkedin-jobs-python-developer.p.rapidapi.com/jobs/"

querystring = {"title":"python developer","place":"Helsinki","post_date":"2023-05-10"}

headers = {
    "content-type": "application/json",
	"X-RapidAPI-Key": token,
	"X-RapidAPI-Host": "linkedin-jobs-python-developer.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
response = requests.request("GET", url, headers=headers, params=querystring)
response = json.loads(response.text)

with open('logfile_1.json', 'w', encoding='utf-8') as fp:
    json.dump(response.json(), fp, indent=2, ensure_ascii=False, sort_keys=True)
