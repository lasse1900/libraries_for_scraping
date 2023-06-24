import pandas
from datetime import datetime as dt
today = dt.today()

# file_params = pandas.read_csv('my_terms.csv',delimiter=',', nrows=1)
# print(file_params)

# print('-'*20)
file_params = pandas.read_csv('search_terms.csv')
keywords = []
for index, row in file_params.iterrows():
    # print(f"index: {index}")
    # print(row['keyword'], row['location'])
    # print(row['keyword'])
    sana = row['keyword']
    keywords.append(sana)

subject = "Open Jobs on Indeed - " + today.strftime("%B %d, %Y")
print(subject)
print(f"keywords: {keywords}")

