# https://www.youtube.com/watch?v=a6fIbtFB46g
# https://github.com/CoreyMSchafer/code_snippets

# https://codebeautify.org/htmlviewer

from requests_html import HTML,  HTMLSession

session = HTMLSession()
r = session.get('https://coreyms.com/')

# print(r.html)
article = r.html.find('article', first=True)
# print(article.html)

headline = article.find('.entry-title-link', first=True).text
print(headline)

summary = article.find('.entry-content p', first=True).text
print(summary)

# vid_src = article.find('iframe', first=True)
# print(vid_src.html)

vid_src = article.find('iframe', first=True).attrs['src']
# print(vid_src)
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
# print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

