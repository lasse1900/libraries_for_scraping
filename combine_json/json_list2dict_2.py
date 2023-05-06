import json

# JSON file path
json_file = 'input1.json'

# Read JSON file with proper decoding
with open(json_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

with open(json_file, 'r', encoding='utf-8') as file:
    json_data2 = json.load(file)

print('-'*25)
print(type(json_data2))
print('-'*25)
print(f"json_data2 is of type: {type(json_data2)}")

# Convert JSON data to dictionary
data_dict = json_data

print(type(data_dict))
data_dict2 = json_data2
print(type(data_dict2))

# Method 1: Using the update() method
merged_object = data_dict.copy()

# merged_object.update(data_dict2)


# # Method 2: Using the unpacking operator (**)
# merged_object = {**json_data, **json_data2}

# # Print the resulting dictionary
# print(data_dict)
# print('-'*25)
# print(data_dict2)

# Convert the merged object to JSON
merged_json = json.dumps(merged_object, indent=4)

# Print the merged JSON
# print(merged_json)