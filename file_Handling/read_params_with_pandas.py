import pandas

# file_params = pandas.read_csv('my_terms.csv',delimiter=',', nrows=1)
# print(file_params)

print('-'*20)
file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    print(f"index: {index}")
    print(row['keyword'], row['location'])

