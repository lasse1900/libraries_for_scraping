# Open the file for reading
with open('file.json', 'r') as file:
    content = file.read()
    print(content)

# Prepend the desired string
# modified_content = '[{ "data": ' + content

# # Open the same file for writing (which overwrites the existing file)
# with open('file.json', 'w') as file:
#     file.write(modified_content)
