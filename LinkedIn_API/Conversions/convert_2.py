import subprocess

# Path to the input JSON file
# json_file_path = '/path/to/input.json'
json_file_path = 'formated.md'

# Path to the output DOCX file
# docx_file_path = '/path/to/output.docx'
docx_file_path = 'output4.docx'

# Pandoc command to convert JSON to DOCX
pandoc_cmd = f'pandoc "{json_file_path}" -o "{docx_file_path}"'

# Execute the Pandoc command using subprocess
subprocess.run(pandoc_cmd, shell=True)
