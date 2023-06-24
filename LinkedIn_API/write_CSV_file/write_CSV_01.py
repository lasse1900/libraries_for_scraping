import csv

# Example variables
name = "John Doe"
age = 30
city = "New York"

locations = ['Tampere', 'Suomi','Tampere']
# Specify the file path and name
csv_file = "output.csv"

# Open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the variable values as a row in the CSV file
    writer.writerow([name, age, city])
    # writer.writerow(locations)

print("Variables saved to CSV successfully.")
