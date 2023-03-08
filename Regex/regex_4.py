import re
# https://www.youtube.com/watch?v=K8L6KVGG-7o
text_to_search = '''
abcdefghijklmnopqrstuvxyz
ABCDEFGHIJKLMNOPQRSTUVXYZ
1234567890


Ha HaHa

MetaCharacters (need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

emails = '''
DaveCMartin@gmail.com
charles.harris@university.edu
corey-321-schafer@my-work.net
'''

sentence = 'Start a sentence and then bring it to an end'


# pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
# pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

# Example (bad manner)
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')


matches = pattern.finditer(emails)

for match in matches:
    print(match)

# with open('adresses.txt','r', encoding='utf-8') as f:
# with open('adresses.txt','r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)





