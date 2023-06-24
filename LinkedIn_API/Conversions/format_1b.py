import json

with open('backup.json', 'r') as file: # Handle JSON as a basic string file !
    data = file.read()

for i in range(10):

    content = json.loads(data)[0]
    print(content)

    def format(key, value):
        return f"<{value}>" if key.endswith("_url") else value

    for key, value in content.items():
        print(f"- {key} : {format(key, value)}")
    print('-'*50)
  