# https://www.youtube.com/watch?v=a6fIbtFB46g
# https://github.com/CoreyMSchafer/code_snippets
# https://www.youtube.com/watch?v=q5uM4VKywbA

# https://codebeautify.org/htmlviewer

import time
from requests_html import HTML,  HTMLSession

session = HTMLSession()

t1 = time.perf_counter()

r = session.get('https://httpbin.org/delay/1')
response = r.html.url
print(response)

r = session.get('https://httpbin.org/delay/2')
response = r.html.url
print(response)

r = session.get('https://httpbin.org/delay/3')
response = r.html.url
print(response)

t2 = time.perf_counter()

print(f'Syncronous: {t2 -t1} seconds')