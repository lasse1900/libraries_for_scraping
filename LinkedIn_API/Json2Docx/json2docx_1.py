import json
from docx import Document

# Load JSON data from a file or API response
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Create a new Word document
document = Document()

# Iterate through JSON data and add content to the document
for item in json_data:
    # Extract the desired data from the JSON item
    # and add it to the document in the desired format
    document.add_paragraph(item['key'] + ': ' + item['value'])

# Save the Word document
document.save('output_1405a.docx')
