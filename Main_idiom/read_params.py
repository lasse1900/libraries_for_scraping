import pandas
row_count = 0
filenames = []
keywords = []
locations = []
offset = 0

file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    # print(f"------> Iterrows # {index}")
    # sana = row['keyword']
    filenames.append(row['filename'])
    keywords.append(row['keyword'])
    locations.append(row['location'])
    keyword_index = index
    # print(row['keyword'], row['location'])
    # print("keyword: ", row['keyword'], " location: ", row['location'])
    row_count = index + 1

# print("-"*30)
print(f"keywords[0] {keywords[0]}")
print(f"filenames {filenames}")
print(f"keywords {keywords}")
print(f"locations {locations}")
print(f"index {index}")