import json

def loadData():
    with open('grades.json') as json_file:
        data = json.load(json_file)
        # print(data)

def topThree():
    info = loadData()
    gradeOrder = sorted(info, key=lambda k: k["grade"], reverse=True)
    gradeOrder = gradeOrder[:3]
    for g in gradeOrder:
        print("{grade} {name}")

# Here's our payoff idiom!
if __name__ == '__main__':
    topThree()
