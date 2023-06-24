
# reads to memory
# context manager automatically closes file

with open('simple.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')
