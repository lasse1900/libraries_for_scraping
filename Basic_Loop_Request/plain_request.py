import requests

url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"

querystring = {"offset":"0","keyword":"python developer","location":"Helsinki"}

headers = {
	"X-RapidAPI-Key": "2c36597583mshb3ec6f540dfd966p181965jsne63a63911509",
	"X-RapidAPI-Host": "indeed-jobs-api-finland.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())