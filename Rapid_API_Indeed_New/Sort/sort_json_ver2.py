
import json
from datetime import datetime

with open('python_developer_suomi.json') as user_file:
    file_contents = json.load(user_file)

if __name__ == "__main__":

    temp = sorted(
        file_contents,
        reverse=True,
        key = lambda x: datetime.strptime(x["date"], '%y-%m-%d')
        # key = lambda x: (x["date"] == "null", x["date"] == "" , x["date"])
    )

    print(type(temp))
    json_dump = json.dumps(temp, indent=2, ensure_ascii=False, sort_keys=True)
    print(json_dump)

    with open('python_sorted.json', 'w', encoding='utf-8') as fp:
        fp.write(json_dump)


