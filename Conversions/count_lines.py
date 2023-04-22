# https://pynative.com/python-count-number-of-lines-in-file/

with open("sorted.json", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)

number_of_jobs = (count - 2)/16
print(f'Number of jobs: {int(number_of_jobs)}')


