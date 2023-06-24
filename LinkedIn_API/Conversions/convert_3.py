import subprocess

# name of the input JSON file
input_file = "example.md"

# name of the output RTF file
output_file = "output.rtf"

# specify the Pandoc command with appropriate arguments
pandoc_command = f"pandoc {input_file} -f markdown -t rtf -o {output_file}"

# run the command using subprocess
subprocess.run(pandoc_command, shell=True)
