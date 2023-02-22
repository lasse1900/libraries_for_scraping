# https://www.youtube.com/watch?v=tb8gHvYlCFs&t=89s
# https://www.youtube.com/watch?v=Uh2ebFW8OYM   - File objects
import requests


# r = requests.get('http://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
r = requests.get('http://httpbin.org/delay/1', timeout=3)

# r = requests.get('http://httpbin.org/delay/6', timeout=3)

# print(r.text)
print(r)