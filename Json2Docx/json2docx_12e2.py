import json
# Open the file for reading
with open('file.json', 'r', encoding='utf8') as file:
    content = file.read()
    data0 = content
    print(data0)

print('-'*25)

with open("sorted.json", encoding='utf-8') as json_file:
    data1 = json.load(json_file)
    print(data1)
    print(data0)
    # temp = data0 + data1
    temp = data0.extend(data1)
    print(temp)

# with open("input_3.json", encoding='utf-8') as json_file:
#     data1 = json.load(json_file)
#     temp = data0 + data1 + data2
#     temp.extend(data1)
# Prepend the desired string
# modified_content = '{}}] '



# # Open the same file for writing (which overwrites the existing file)
# with open('file.json', 'a') as file:
#     file.write(data)
