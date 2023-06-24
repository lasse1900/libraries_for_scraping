import json

def read_json_file(filename):
    with open(filename, encoding="utf-8") as json_file:
        return json.load(json_file)

data_for_all_files = [read_json_file(name) for name in ["input1.json", "input2.json", "input3.json", "input4.json"]]
print(data_for_all_files)


