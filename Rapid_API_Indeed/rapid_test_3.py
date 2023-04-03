import requests
import os
import json
from dotenv import load_dotenv
import time

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api.p.rapidapi.com/indeed-us/"

headers = {
	"X-RapidAPI-Key": token,
	"X-RapidAPI-Host": "indeed-jobs-api.p.rapidapi.com"
}
endpoint = 20
# for offset in range(0, 641, 10):
with open('logfile_by_macro_3.json', 'a+', encoding='utf-8') as fp:
	for offset in range(0, 10, 10):

		# querystring = {"offset":f"{offset}","keyword":"flutter","location":"california"}
		querystring = {"offset":"0","keyword":"python developer","location":"california"}		

		response = requests.request("GET", url, headers=headers, params=querystring)

		print(response.text)
		json.dump(response.json(), fp, indent=2, ensure_ascii=False, sort_keys=True)
		time.sleep(70)
