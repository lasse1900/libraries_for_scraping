
# context manager automatically closes file
# less momery usage, not reading into memory

with open('simple.txt', 'r') as f:

    for line in f:
        print(line, end='')


