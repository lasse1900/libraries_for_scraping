import json
import requests

url = "https://tools.learningcontainer.com/sample-json.json"

response = requests.get(url)
dic = json.loads(response.text)

print(dic)

# dic={
#     "name": "John O. Smith",
#     "age": 30,
#     "id": '12345'
# },
# {
#     "name": "Ann Smith",
#     "age": 29,
#     "id": '12322'
# }


json_obj = json.dumps(dic, indent=4)

with open("output.txt", "w") as f:
    f.write(json_obj)

