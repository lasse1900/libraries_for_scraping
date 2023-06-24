import requests
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("X-RapidAPI-Key")

url = "https://linkedin-jobs-python-developer.p.rapidapi.com/jobs/"

querystring = {"title":"python developer","place":"stocholm","post_date":"2023-03-17"}

headers = {
	"X-RapidAPI-Key": token,
	"X-RapidAPI-Host": "linkedin-jobs-python-developer.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())