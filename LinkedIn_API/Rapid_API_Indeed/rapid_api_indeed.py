import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api.p.rapidapi.com/indeed-us/"

headers = {
	"X-RapidAPI-Key": token,
	"X-RapidAPI-Host": "indeed-jobs-api.p.rapidapi.com"
}

querystring = {"offset":"0","keyword":"python","location":"Helsinki"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)