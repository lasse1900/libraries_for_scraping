#!/bin/bash

python request_jobs.py 0 django_tre.json django tampere
python request_jobs.py 0 pythonDeveloper_tre.json "python developer" tampere

echo "Hi, I'm sleeping for 5 seconds..." 
sleep 5

python append_json_files.py
