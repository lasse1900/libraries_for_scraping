import pandas
from api_request import main # running API-request

# request open jobs with keywords given in search_terms.csv file
row_count = 0
filenames = []
keywords = []
locations = []
offset = 0


file_params = pandas.read_csv('search_terms_2.csv')
for index, row in file_params.iterrows():
    keyword = row['keyword']
    keyword_stripped =keyword.strip()
    keywords.append(keyword_stripped)
    location = row['location']
    location_stripped = location.strip()
    locations.append(location_stripped)   

    # print(f"offset: {offset},input_{index}.json,{row['keyword']},{row['location']}")
    print(f"offset: {offset}, input_{index}.json, {keywords[index]}, {locations[index]}")
    main(offset, f"input_{index}.json", f"{keywords[index]}", f"{locations[index]}")
    row_count = index + 1