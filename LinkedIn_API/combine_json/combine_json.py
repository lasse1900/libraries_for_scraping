import json

def append_json_files(input_file1, input_file2, output_file):
    # Load the contents of the first JSON file
    with open(input_file1, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)
        print(data1)

    # Load the contents of the second JSON file
    with open(input_file2, 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
        print(data2)

    # Merge the two JSON objects
    merged_data = {**data1, **data2}

    # Write the merged JSON data to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(merged_data, outfile, ensure_ascii=False)

# Replace 'input1.json', 'input2.json', and 'output.json' with your actual file names
input_file1 = 'input1.json'
input_file2 = 'input2.json'
output_file = 'output.json'

append_json_files(input_file1, input_file2, output_file)

