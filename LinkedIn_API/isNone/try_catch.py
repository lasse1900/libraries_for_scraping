import pandas
import math

# request open jobs with keywords given in search_terms.csv file
row_count = 0
filenames = []
keywords = []
locations = []
offset = 0
location = ''

file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    location = row['location']
    locations.append(location)  
    try: 
        if math.isnan(location):
            location = 'Suomi'
            print(f"location set to default: {location}")
    except:
        print(f"location given as csv-file input: {location}")
        # print("The variable is not NaN.")


