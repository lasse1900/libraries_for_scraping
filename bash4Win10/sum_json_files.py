import json

def read_json_file(filename):
    with open(filename, encoding="utf-8") as json_file:
        return json.load(json_file)

data_for_all_files = [read_json_file(name) for name in ["input_0.json", "input_1.json"]]

print(data_for_all_files)