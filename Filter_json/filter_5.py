import json
import datetime

with open('sorted.json') as json_file:
    data = json.load(json_file)

filtered_data = [obj for obj in data if obj.get("date") > "1-4-23"]
print(filtered_data)

with open('filtered.json', 'w', encoding='utf-8') as fp:
    json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)