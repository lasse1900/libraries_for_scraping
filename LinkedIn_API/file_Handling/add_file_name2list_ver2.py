filenames = []  # create an empty list for the filenames

row_count = 4

# add a filename to the list using the append() method
# filename = "example.txt"
# filenames.append(filename)

# add more filenames to the list according to keywords row count
for i in range(row_count):
    filenames.append(f"input_{i}.json")

print(filenames)  # prints ["example.txt", "file1.txt", "file2.txt"]
