import os
# https://stackoverflow.com/questions/32175727/check-if-files-from-multiple-filelists-exist-in-given-directory
# List of file paths
file_paths = [
    'input_0.json',
    'input_1.json',
    'input_2.json',
    'input_3b.json',
]

error = False
# Check existence of each file
for file_path in file_paths:
    if os.path.exists(file_path):
        print(f"{file_path} exists")
    else:
        print(f"{file_path} does not exist")
        error = True

if(error != True):
    print("Let's go on ")
else:
    print("Stop here!")