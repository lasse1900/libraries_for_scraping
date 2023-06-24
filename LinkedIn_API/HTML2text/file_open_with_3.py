
# reads to memory
# context manager automatically closes file
# https://www.youtube.com/watch?v=Uh2ebFW8OYM

with open('simple.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

