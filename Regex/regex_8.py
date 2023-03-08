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
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'Start')

# pattern = re.compile(r'[Ss][Tt][Aa]')
pattern = re.compile(r'start', re.IGNORECASE)

matches = pattern.search(sentence)

print(matches)
# print(pattern)

