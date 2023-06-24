import json
import io
import codecs

f = io.open("blacklist.json", mode="r", encoding="utf-8")

print(f.read(), '---')

string1 = f.read()
print(type(string1))


# res = string1.strip().split(', ')
res = f.read()

# print(string1)

# print(type(lista))
# print(lista)

# printing final result and its type
print ("final list", res)
print (type(res))

