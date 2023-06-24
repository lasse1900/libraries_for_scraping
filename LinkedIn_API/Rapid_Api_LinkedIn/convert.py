import ast
import pprint
import json


d = ast.literal_eval(open("logfile.log", encoding="iso-8859-1").read())
pprint(json.dumps(d, indent=2))

input_out = json.dumps(d, indent=2)

# for x in range(len(input_out)):
#     outfile = open('logfile_abb.log', 'w')
#     print((input_out[x]), file=outfile)
#     outfile.close()

# with open('logfile.json', 'w') as file:
#   file.write(json.dumps(d, indent=2))

with open('logfile.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)