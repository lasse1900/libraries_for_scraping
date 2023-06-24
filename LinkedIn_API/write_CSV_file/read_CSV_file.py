import csv

# Specify the file path and name
csv_file = "data.csv"

# Initialize an empty string to store the data
data_string = ""

# Open the CSV file in read mode
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        # Join the values of each row into a string
        row_string = ','.join(row)
        
        # Append the row string to the data string
        data_string += row_string + '\n'

# print("Data read from CSV:\n", data_string)
print(data_string)
