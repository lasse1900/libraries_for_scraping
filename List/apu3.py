# -*- encoding: utf-8 -*-

# converting a unknown formatting file in utf-8

import codecs
# import commands
import subprocess

file_location = "blacklist.json"
file_encoding = subprocess.getoutput('file -b --mime-encoding %s' % file_location)

file_stream = codecs.open(file_location, 'r', file_encoding)
file_output = codecs.open(file_location+"b", 'w', 'utf-8')

for l in file_stream:
    file_output.write(l)

file_stream.close()
file_output.close()