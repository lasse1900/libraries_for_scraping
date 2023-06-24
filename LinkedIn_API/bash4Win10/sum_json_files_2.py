import json
import pathlib
import itertools
input_files = ["input_0.json", "input_1.json"]
input_data = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in input_files]
output_data = list(itertools.chain(*input_data))
pathlib.Path("output.json").write_text(json.dumps(output_data), encoding="utf-8")