import json
import pypandoc

with open('sorted_with_header.json', 'r') as file:
    data = file.read()

    print(type(data))
    # obj = json.load(file)
    print(len(data))

with open("formated.md", "w") as wf:
    for i in range(10):
    

        content = json.loads(data)[i]
        print(content)

        def format(key, value):
            return f"<{value}>" if key.endswith("_url") else value

        for key, value in content.items():
            wf.write(f"- {key} : {format(key, value)}")

# pandoc formated.md -f markdown -t docx -o example.docx