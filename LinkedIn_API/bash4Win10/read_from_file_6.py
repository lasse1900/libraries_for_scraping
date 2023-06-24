import time
import json
import os
import pandas
import pathlib
import itertools
from request_jobs import load_jobs
from sort_json import sort
from format_json import format_2_docx
from send_email_to_csv_contacts_once_a_day import send_email

# delete old files
if os.path.exists("input_0.json"):
    os.remove("input_0.json")
if os.path.exists("input_1.json"):
    os.remove("input_1.json")
if os.path.exists("input_2.json"):
    os.remove("input_2.json")
if os.path.exists("input_3.json"):
    os.remove("input_3.json")

# open file in read mode
# https://pynative.com/python-count-number-of-lines-in-file/
with open(r"search_terms.csv", 'r') as fp:
    for line_count, line in enumerate(fp):
        pass
print('Total line count', line_count + 1)

for x in range(0, line_count - 1):
    input_files = []  # create an empty list for the input_files
    # add a filename to the list using the append() method
    filename = f"input_{x}.json"
    input_files.append(filename)
    print(input_files)

# request open jobs with keyword 1
file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    print(row['keyword'])
    print(row['location'])
    load_jobs(f"input_{index}.json", row['keyword'], row['location'])

time.sleep(5)
print("Hi, I'm appending files for 5 seconds..." )
input_data = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in input_files]
output_data = list(itertools.chain(*input_data))
# pathlib.Path("output.json").write_text(json.dumps(output_data), encoding="utf-8", indent=2, ensure_ascii=False, sort_keys=True)
pathlib.Path("output.json").write_text(json.dumps(output_data), encoding="utf-8")

time.sleep(5)
print("Hi, I'm sorting files for 5 seconds...")
# sort json file according to descending date
sort()
time.sleep(2)
print("Hi, I'm formating json to docx for 5 seconds...")
# formating json file into word document
format_2_docx()
time.sleep(2)
print("Hi, I'm sending email..." )
# sending jobs.docx according to the contacts.csv mailing list
send_email()