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

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'^St')

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
# pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') OR !
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')



# pattern = re.compile(r'end$') # Search from sentence

matches = pattern.finditer(text_to_search)
# matches = pattern.finditer(sentence)

for match in matches:
    print(match)

# with open('adresses.txt','r', encoding='utf-8') as f:
# with open('adresses.txt','r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)





