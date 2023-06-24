import json
import datetime

with open('sorted_short.json') as json_file:
    data = json.load(json_file)

filtered_data = [obj for obj in data if obj.get("date") > "2023-4-1"]
print(filtered_data)