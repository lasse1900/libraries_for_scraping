
import json
from datetime import datetime
# https://www.youtube.com/watch?v=00JL7QfWPC0&t=30s

with open('python_developer_suomi.json') as user_file:
    file_contents = json.load(user_file)

if __name__ == "__main__":

    temp = sorted(
        file_contents,
        reverse=True,
        key = lambda x: datetime.strptime(x["date"], '%d-%m-%y')
        # key = lambda x: (x["date"] == "null", x["date"] == "" , x["date"])
        # key = lambda x: (x["date"] == "null", x["date"] == "" , datetime.strptime(x["date"], '%d-%m-%y')) 
            ## ValueError: time data '' does not match format '%d-%m-%y' when input data == null
    )

    print(type(temp))
    json_dump = json.dumps(temp, indent=2, ensure_ascii=False, sort_keys=True)
    print(json_dump)

    with open('python_sorted_3.json', 'w', encoding='utf-8') as fp:
        fp.write(json_dump)


