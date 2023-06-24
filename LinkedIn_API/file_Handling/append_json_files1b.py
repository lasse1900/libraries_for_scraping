import json

# TODO get the number of files as an argument
def parse_json_files_together():
    print("append files")
    
    def write_json(data, filename="output.json"):
        print('Here ->')
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    with open("input_0.json", encoding='utf-8') as json_file:
        data0 = json.load(json_file)

    with open("input_1.json", encoding='utf-8') as json_file:
        data1 = json.load(json_file)

    with open("input_2.json", encoding='utf-8') as json_file:
        data2 = json.load(json_file)
        temp = data0 + data1
        temp.extend(data2)

    write_json(temp)

    if __name__ == "__main__":
        parse_json_files_together()