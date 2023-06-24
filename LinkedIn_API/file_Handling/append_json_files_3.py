import json

# TODO get the number of files as an argument
# def parse_json_files_together(row_count=3):
row_count = 4

index = range(row_count-1)
for i in index:
    print(f"input_{i}.json")
    with open(f"input_{i}.json", encoding='utf-8') as json_file:
        data = json.load(json_file)
        temp = data
        temp.extend(data)

    # print(f"ulos -> input_{row_count-1}.json")
    f = open(f"input_{row_count-1}.json", "w")
    f.close()
    with open(f"input_{row_count-1}.json", encoding='utf-8') as json_file:
        data2 = json.load(json_file)
        temp = data
        temp.extend(data2)
