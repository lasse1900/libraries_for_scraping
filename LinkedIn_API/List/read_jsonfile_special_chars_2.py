import json
import codecs

# https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python?rq=1


with open('blacklist.json', 'r') as f:
    lista = json.load(f)
    print(type(lista))
    print(lista)

#f = codecs.open("blacklist.json", "r", "utf-8")

# lista2 = f.read()
# print(lista2)
# lista3 = json(lista2)


# lines = open('blacklist.json', mode='r', buffering=-1, 
#       encoding='utf-8', errors=None, newline=None, 
#       closefd=True, opener=None)

# print(lines)

print (open('blacklist.json').read().encode("utf-8"))