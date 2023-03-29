import requests

url = "https://linkedin-jobs-search.p.rapidapi.com/"

payload = {
	"search_terms": "embedded",
	"location": "Helsinki",
	"page": "1"
}
headers = {
	"content-type": "application/json",
    "X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com",
	"X-RapidAPI-Key": "xxx"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)