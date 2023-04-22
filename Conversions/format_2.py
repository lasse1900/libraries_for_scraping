import json
# NOT working

with open('jobs_data.json') as user_file:
    file_contents = json.load(user_file)


def format(key, value):
    return f"<{value}>" if key.endswith("_url") else value


with open("output.md","w") as fp:
    for key, value in file_contents.items():
        fp.write(f"- {key} : {format(key, value)}")