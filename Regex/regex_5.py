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


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match)
    # print(match.group(2))



