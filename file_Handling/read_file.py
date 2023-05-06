# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

keywords = []
i=0
with open("my_terms_1.txt") as file:
    lines = [line.rstrip() for line in file]
    print(lines[i])
    # print(lines[0])
    # print(lines[1])
    keywords.append(lines[0])
    keywords.append(lines[1])

print(keywords)