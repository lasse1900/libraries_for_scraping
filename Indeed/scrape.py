import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    url = f'https://fi.indeed.com/jobs?q=python+developer={page}'
    r = requests.get(url, headers)
    return r.status_code

print(extract(0))

