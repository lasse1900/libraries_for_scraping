import sys
# https://gitlab.com/Vashinator/call-python-from-bash-script/-/tree/main

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument sent:', str(sys.argv[1]))
file1 = "test.json"
print(f"file name: {file1}")

