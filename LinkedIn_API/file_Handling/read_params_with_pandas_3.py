import pandas

row_count = 0
keywords = []
file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    print(f"index: {index}")
    print(row['keyword'])

    row_count = index + 1
    keyword_index = index
    sana = row['keyword']
    print("-> ",keyword_index)
    keywords.append(sana)

print(f"row count: {row_count}")
print(f"keywords: {keywords}")
print(keywords[index])
