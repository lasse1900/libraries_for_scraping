import json
from datetime import datetime

def loadData():
    with open('python_developer_suomi.json') as user_file:
        file_contents = json.load(user_file)
    return file_contents

def sort():
    info = loadData()
    temp = sorted(
        info,
        reverse=True,
        key = lambda x: datetime.strptime(x["date"], '%d-%m-%y')
        # key = lambda x: (x["date"] == "null", x["date"] == "" , x["date"])
    )

    print(type(temp))
    json_dump = json.dumps(temp, indent=2, ensure_ascii=False, sort_keys=True)
    print(json_dump)

    with open('python_sorted_5.json', 'w', encoding='utf-8') as fp:
        fp.write(json_dump)

sort()