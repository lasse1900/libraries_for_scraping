import json

heading = {
    "sections": []
}

# Open the file in write mode
with open('heading.json', 'w') as file:
    # Write the heading to the file
    json.dump(heading, file)
