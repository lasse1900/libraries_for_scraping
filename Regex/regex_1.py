import re
# https://www.youtube.com/watch?v=K8L6KVGG-7o
# https://www.youtube.com/watch?v=sa-TUpSx1JA
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

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
M. T
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'^St')

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')



# pattern = re.compile(r'end$') # Search from sentence

matches = pattern.finditer(text_to_search)
# matches = pattern.finditer(sentence)


for match in matches:
    print(match)

# print(text_to_search[1:4])




