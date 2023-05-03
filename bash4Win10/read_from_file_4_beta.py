import time
import json
import os
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

# get the amount of argument lines
with open(r"search_terms.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)

# request open jobs with keyword 1
with open("search_terms.txt") as file:
    lines = [line.rstrip() for line in file]
    print(lines[0])
    load_jobs("input_0.json", lines[0])
    print(lines[1])
    load_jobs("input_1.json", lines[1])
    print(lines[2])
    load_jobs("input_2.json", lines[2])
    print(lines[3])
    load_jobs("input_3.json", lines[3])

time.sleep(5)
print("Hi, I'm appending files for 5 seconds..." )

def write_json(data, filename="output.json"):
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

with open("input_0.json", encoding='utf-8') as json_file:
    data = json.load(json_file)

with open("input_1.json", encoding='utf-8') as json_file:
    data2 = json.load(json_file)
    temp = data
    temp.extend(data2)

with open("input_2.json", encoding='utf-8') as json_file:
    data3 = json.load(json_file)
    temp = data
    temp.extend(data3)

with open("input_3.json", encoding='utf-8') as json_file:
    data4 = json.load(json_file)
    temp = data
    temp.extend(data4)

write_json(data)

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

