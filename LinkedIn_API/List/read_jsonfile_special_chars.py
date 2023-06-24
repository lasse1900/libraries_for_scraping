import json

# with open('example.json', 'r') as f:
#         data = json.load(f)
    
# string = data.get('content', '')
# print(string)

# print('-'* 20)



with open('blacklist.json', 'r') as f:
    lista = json.load(f)
    print(type(lista))
    print(lista)