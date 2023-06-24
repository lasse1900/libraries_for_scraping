import json

# JSON list
json_list = [
    {"key1": "value1"},
    {"key2": "value2"},
    {"key3": "value3"}
]

with open("input1.json", 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)
    print(data1)
    print(type(data1))
    print('-'*30)

# Convert JSON list to dictionary
result_dict = {}
for item in json_list:
    result_dict.update(item)

result_dict_2 = {}
for item in data1:
    result_dict.update(item)

# Alternatively, you can use a dictionary comprehension
result_dict_3 = {key: value for item in data1 for key, value in item.items()}

# Print the resulting dictionary
# print(result_dict)
print('-'*30)
print(result_dict_2)
print('-'*30)
print(result_dict_3)

