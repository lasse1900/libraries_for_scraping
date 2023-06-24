import ast
import pprint
import json


d = ast.literal_eval(open("logfile_2.log", encoding="iso-8859-1").read())
pprint.pprint(d)

# print(json.dumps(d, indent=2))

# input_out = json.dumps(d, indent=2)

# # for x in range(len(input_out)):
# #     outfile = open('logfile_abb.log', 'w')
# #     print((input_out[x]), file=outfile)
# #     outfile.close()

# with open('logfile.json', 'w') as file:
#   file.write(json.dumps(d, indent=2))