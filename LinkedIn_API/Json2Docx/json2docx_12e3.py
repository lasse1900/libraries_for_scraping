import json

# Open the JSON file for reading
with open('filtered.json', 'r') as file:
    json_data = json.load(file)

# Add the desired clause at the beginning
modified_data = [{'data': json_data}]

# Open the same JSON file for writing (which overwrites the existing file)
with open('data.json', 'w') as file:
    json.dump(modified_data, file, indent=4)
