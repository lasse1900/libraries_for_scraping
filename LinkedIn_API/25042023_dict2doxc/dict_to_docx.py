import docx

# Define your dictionary
my_dict = {"Name": "John", "Age": 30, "Occupation": "Software Engineer"}

# Create a new Word document
doc = docx.Document()

# Loop through the dictionary and add each key-value pair as a paragraph to the Word document
for key, value in my_dict.items():
    doc.add_paragraph(key + ": " + str(value))

# Save the document
doc.save("my_document.docx")
