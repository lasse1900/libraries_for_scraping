import json

# JSON objects to be merged
json_object1 = {
    "key1": "value1",
    "key2": "value2"
}

json_object2 = {
    "key3": "value3",
    "key4": "value4"
}

# Method 1: Using the update() method
merged_object = json_object1.copy()
merged_object.update(json_object2)

# Method 2: Using the unpacking operator (**)
merged_object = {**json_object1, **json_object2}

# Convert the merged object to JSON
merged_json = json.dumps(merged_object, indent=4)

# Print the merged JSON
print(merged_json)
