import json
import pathlib
import itertools
    
def parse_json_files_together():
    file_paths = []  # create an empty list for the needed filenames
    file_paths = ["request_loop4a.json", "request_loop4b.json"]
    input_data = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in file_paths]
    output_data = list(itertools.chain(*input_data))
    pathlib.Path("output_temp.json").write_text(json.dumps(output_data), encoding="utf-8")

    with open(f"output_final.json", 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    parse_json_files_together()