import json
import pathlib
import itertools


input_files = ["input_0.json", "input_1.json", "input_2.json", "input_3.json"]
input_data = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in input_files]
output_data = list(itertools.chain(*input_data))
pathlib.Path("output_temp.json").write_text(json.dumps(output_data), encoding="utf-8")

# print(output_data)
# print(type(output_data))

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

# with open('logfile_1.json', 'w', encoding='utf-8') as fp:
#     json.dump(output_data.json(), fp, indent=2, ensure_ascii=False, sort_keys=True)