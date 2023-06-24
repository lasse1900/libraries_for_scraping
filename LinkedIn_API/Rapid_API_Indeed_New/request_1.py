import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")

url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"

querystring = {"offset":"0","keyword":"python developer","location":"Helsinki"}

headers = {
	"X-RapidAPI-Key": token,
	"X-RapidAPI-Host": "indeed-jobs-api-finland.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)