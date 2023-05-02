import time
import json
import os
from request_jobs import load_jobs
from sort_json import sort
from format_json import format_2_docx
from send_email_to_csv_contacts_once_a_day import send_email

# delete old files
if os.path.exists("input_1.json"):
    os.remove("input_1.json")
if os.path.exists("input_2.json"):
    os.remove("input_2.json")

# request open jobs with keyword 1
for line in open("my_terms_1.txt"):
    term = line.strip()
    print(term)
    load_jobs("input_1.json", term)
    # file.close()

# request open jobs with keyword 2
for line in open("my_terms_2.txt"):
    term = line.strip()
    print(term)
    load_jobs("input_2.json", term)

time.sleep(5)
print("Hi, I'm appending files for 5 seconds..." )

def write_json(data, filename="output.json"):
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

with open("input_1.json", encoding='utf-8') as json_file:
    data = json.load(json_file)

with open("input_2.json", encoding='utf-8') as json_file:
    data2 = json.load(json_file)
    temp = data
    temp.extend(data2)

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

