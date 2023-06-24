import json
import datetime

with open('sorted_short.json') as json_file:
    data = json.load(json_file)

# Specify the desired date
desired_date = datetime.datetime(2023, 5, 1)
# desired_date = datetime.datetime(1, 4, 23)

# Filter objects based on date, JSON date format: [{"date": "11-04-23"}],
filtered_objects = [obj for obj in data if datetime.datetime.strptime(obj['date'], '%Y-%m-%d') > desired_date]
# filtered_objects = [obj for obj in data if datetime.datetime.strptime(obj['date'], '%d-%m-%y') > desired_date]
# print(filtered_objects)

with open('filtered.json', 'w', encoding='utf-8') as fp:
    json.dump(filtered_objects, fp, indent=2, ensure_ascii=False, sort_keys=True)
