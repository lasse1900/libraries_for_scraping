import json

def write_json(data, filename="output.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

with open("django_tre.json") as json_file:
    data = json.load(json_file)
with open("pythonDeveloper_tre.json") as json_file:
    data2 = json.load(json_file)
    temp = data
    temp.extend(data2)

write_json(data)