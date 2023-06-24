
# Python program to
# demonstrate reading files
# using for loop
 
# L = ["Geeks\n", "for\n", "Geeks\n"]
 
# # Writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()
 
# Opening file
# file1 = open('myfile.txt', 'r')


file1 = open('data.csv', 'r')
count = 0
 
# Using for loop
# print("Using for loop")
for line in file1:
    count += 1
    # print("Line{}: {}".format(count, line.strip()))
    print(line.strip())
    locations_updated = line.strip()
 

print(locations_updated)
# Closing files
file1.close()