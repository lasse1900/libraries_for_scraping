# open file in read mode
with open(r"contacs.csv", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)