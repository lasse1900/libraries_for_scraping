# https://stackoverflow.com/questions/27315472/how-to-count-items-in-json-data

import json
with open('movie.json', encoding='utf8') as JSONFile:
    data = json.load(JSONFile)
print(len(data['movie'][0]))

