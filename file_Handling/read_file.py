# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

with open("my_terms_1.txt") as file:
    lines = [line.rstrip() for line in file]
    print(lines[0])
    print(lines[1])