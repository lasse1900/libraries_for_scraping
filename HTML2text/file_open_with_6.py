
# reads to memory
# context manager automatically closes file

with open('simple.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

