# https://www.youtube.com/watch?v=a6fIbtFB46g
# https://github.com/CoreyMSchafer/code_snippets
# https://www.youtube.com/watch?v=q5uM4VKywbA

# https://codebeautify.org/htmlviewer

import csv
from requests_html import HTML,  HTMLSession

with open('simple_2.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()


match = html.find('#footer', first=True)
print(match)
