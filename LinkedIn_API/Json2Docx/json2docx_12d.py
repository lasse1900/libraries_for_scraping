import json

# Open the JSON file for reading
with open('data_0.json', 'r') as file:
    json_data = json.load(file)

# Modify the header information
json_data['header'] = '[{ "data": '

# Open the same JSON file for writing (which overwrites the existing file)
with open('data_77.json', 'w') as file:
    json.dump(json_data, file, indent=4)
