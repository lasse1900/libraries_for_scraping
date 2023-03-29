import ast
import pprint
import json


d = ast.literal_eval(open("logfile_2.log", encoding="iso-8859-1").read())
pprint.pprint(d)

# print(json.dumps(d, indent=2))

