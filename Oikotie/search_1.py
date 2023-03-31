import requests

sequenceId = 1

url = 'https://api.schibsted.com/finn/job/easyapply/apip/application/{sequenceId}'
req = requests.get(url)

print(req.status_code)
print(req.headers)
print(req.text)