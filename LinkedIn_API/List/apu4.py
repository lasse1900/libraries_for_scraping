import json
# array = '{"fruits": ["apple", "banana", "orange"]}'
array = ["apple", "banana", "orange"]
data  = json.loads(array)
fruits_list = data
print(fruits_list)