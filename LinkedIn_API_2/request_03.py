import requests
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("X-RapidAPI-Key")

url = "https://linkedin-jobs-python-developer.p.rapidapi.com/jobs/"

querystring = {"place":"munich","title":"python developer","company":"facebook","post_date":"2023-05-17"}

headers = {
	"X-RapidAPI-Key": token,
	"X-RapidAPI-Host": "linkedin-jobs-python-developer.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())