#!/bin/bash

sleep 5
#      argv 1          argv 2       argv 3             argv 4

# python request_jobs.py input_1.json <(cat file.txt)
python request_jobs.py input_1.json $(cut -f 5 -d , <tiedosto.txt)