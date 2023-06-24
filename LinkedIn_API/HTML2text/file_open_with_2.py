
# reads to memory
# context manager automatically closes file

with open('simple.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

