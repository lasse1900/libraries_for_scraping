import json
import pypandoc

# Formating JSON as MD to docx
# Skandic alphabeths fail
# pandoc formated.md -f markdown -t docx -o example.docx (command line)
# pandoc formated.json -f json -t docx -o example.docx

with open('sorted_with_header.json', 'r') as file:
    data = file.read()

with open("formated.md", "w") as wf:
        # https://stackoverflow.com/questions/49343570/how-can-i-find-the-length-of-a-json-file
        # counting length -> i
    for i in range(10):
    

        content = json.loads(data)[i]
        print(content)

        def format(key, value):
            return f"<{value}>" if key.endswith("_url") else value

        for key, value in content.items():
            wf.write(f"- {key} : {format(key, value)}")

input_file = "formated.md"
output_file = "output2.docx"

output = pypandoc.convert_file(input_file, "docx", outputfile=output_file)
