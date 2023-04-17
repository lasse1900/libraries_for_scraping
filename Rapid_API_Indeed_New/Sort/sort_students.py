import json

def loadData():
    with open('students.json') as user_file:
        file_contents = json.load(user_file)
    return file_contents

def sort():
    info = loadData()
    gradeOrder = sorted(info, key=lambda k: k["grade"], reverse= True)
    gradeOrder = gradeOrder[:4]
    for g in gradeOrder:
        print("{grade} {name}".format(**g))

    print(type(gradeOrder))
    json_dump = json.dumps(gradeOrder, indent=2, ensure_ascii=False, sort_keys=True)
    print(json_dump)

    with open('python_sorted_77.json', 'w', encoding='utf-8') as fp:
        fp.write(json_dump)

sort()