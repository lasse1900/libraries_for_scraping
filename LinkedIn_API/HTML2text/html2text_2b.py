
# doesn't read in memory

with open('simple.txt', 'r') as f:

    for line in f:
        print(line, end='')

