# https://www.youtube.com/watch?v=tb8gHvYlCFs&t=89s
# https://www.youtube.com/watch?v=Uh2ebFW8OYM   - File objects
import requests

# r = requests.get('https://xkcd.com/353')
# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# payload = {'page': 2, 'counr': 25}

payload = {'username': 'Lasse', 'password': 'testing'}
# r = requests.get('http://httpbin.org/get', params=payload)
r = requests.post('http://httpbin.org/post', data=payload)

# print((r.text))
# print((r.content))

# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# print(r.status_code)
# print(r.ok)

# print(r.headers)
#print(r.text)
# print(r.url)
r_dict = r.json()
# print(r.json())
print(r_dict['form'])