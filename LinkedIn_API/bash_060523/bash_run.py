import subprocess

# Replace 'script.sh' with the path to your actual Bash script
script_path = 'script.sh'

# Run the Bash script using the 'bash' command
process = subprocess.Popen(['bash', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the process to finish and get the output
output, error = process.communicate()

# Decode the output and error messages
output = output.decode('utf-8')
error = error.decode('utf-8')

# Print the output and error messages
print("Output:")
print(output)

print("Error:")
print(error)

# Get the return code of the process
return_code = process.returncode
print("Return Code:", return_code)
