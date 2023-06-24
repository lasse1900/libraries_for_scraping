import json

with open('grades.json') as json_file:
    data = json.load(json_file)

filtered_data = [obj for obj in data if obj.get("grade") > 8]
print(filtered_data)