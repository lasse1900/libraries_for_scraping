import sys
import subprocess

for line in open("my_terms.txt"):
    term = line.strip()
    subprocess.check_call([sys.executable, "input1.json", term])