import json

def loadData():
    with open('students.json') as user_file:
        file_contents = json.load(user_file)
    return file_contents

def topFive():
    info = loadData()
    gradeOrder = sorted(info, key=lambda k: k["grade"], reverse= True)
    gradeOrder = gradeOrder[:3]
    for g in gradeOrder:
        print("{grade} {name}".format(**g))

topFive()