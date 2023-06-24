import json

# Open the JSON file for reading
with open('filtered.json', 'r') as file:
    json_data = json.load(file)

# Modify the header information
json_data['header'] = 'New Header'
json_data['subtitle'] = 'New Subtitle'

# Open the same JSON file for writing (which overwrites the existing file)
with open('data_filtered.json', 'w') as file:
    json.dump(json_data, file, indent=4)
