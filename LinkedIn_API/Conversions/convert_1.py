import pypandoc

# input_file = "formated.md"
output_file = "output2.docx"

# output = pypandoc.convert_file(input_file, "markdown", outputfile=output_file)
# output = pypandoc.convert_file("formated.json", "docx", outputfile=output_file)
output = pypandoc.convert_file("dict-to-md.md", "docx", outputfile=output_file)