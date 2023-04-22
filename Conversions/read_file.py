# https://www.youtube.com/watch?v=Uh2ebFW8OYM

# f = open("textfile.txt", "r")
# print(f.name, " ", f.mode)
# f.close()

# with open("textfile.txt", "rb") as f:
#     contents = f.readline()
#     print(contents, end='')

#     contents = f.readline()
#     print(contents, end='')

# with open("textfile.txt", "r") as f:
#     for line in f:
#         print(line, end='')

with open("textfile.txt", "r") as f:
    size_to_read = 10

    contents = f.read(size_to_read)
    print(contents, end='*')

    # print(f.tell())
    f.seek(0)

    contents = f.read(size_to_read)
    print(contents, end='*')

    # while len(contents) > 0:
    #     print(contents, end='*')
    #     contents = f.read(size_to_read)

