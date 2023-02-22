# https://www.youtube.com/watch?v=a6fIbtFB46g
# https://github.com/CoreyMSchafer/code_snippets
# https://www.youtube.com/watch?v=q5uM4VKywbA

# https://codebeautify.org/htmlviewer

import time
from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()


async def get_delay1():
    r = await asession.get('https://httpbin.org/delay/1')
    return r

async def get_delay2():
    r = await asession.get('https://httpbin.org/delay/2')
    return r


async def get_delay3():
    r = await asession.get('https://httpbin.org/delay/3')
    return r

t1 = time.perf_counter()

results = asession.run(get_delay1, get_delay2, get_delay3)

for result in results:
    response = result.html.url
    print(response)


t2 = time.perf_counter()

print(f'Asyncronous: {t2 -t1} seconds')