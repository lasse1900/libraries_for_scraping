import json

# https://www.youtube.com/watch?v=9N6a-VLBa2I&t=6s

with open('sorted_header.json') as user_file:
    file_contents = json.load(user_file)

print(type(file_contents)) # dict

for job in file_contents['Jobs']:
    print(job['company_name'], job['job_location'], job['date'])
    print(job['job_url'])