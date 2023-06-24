# import pandas as pd

# # Specify the file path and name
# csv_file = "data.csv"

# # Read the CSV file using pandas
# data = pd.read_csv(csv_file)

# # Extract the string from the DataFrame
# data_string = data.iloc[0:]

# # print("Data read from CSV:\n", data_string)
# print(data_string)

import pandas as pd

# Specify the file path and name
csv_file = "data.csv"

# Read the CSV file without a header line
data = pd.read_csv(csv_file, header=None)

# Access the data as needed
for row in data.iterrows():
    print(row)

# Access specific values
first_value = data.iloc[0, 0]
print("First value:", first_value)
