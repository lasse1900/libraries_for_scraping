# https://www.youtube.com/watch?v=a6fIbtFB46g
# https://github.com/CoreyMSchafer/code_snippets
# https://www.youtube.com/watch?v=q5uM4VKywbA

# https://codebeautify.org/htmlviewer

import csv
from requests_html import HTML,  HTMLSession

csv_file = open('csm_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

session = HTMLSession()
r = session.get('https://coreyms.com/')

# print(r.html)
articles = r.html.find('article')
# print(article.html)

for article in articles:

    headline = article.find('.entry-title-link', first=True).text
    print(headline)

    summary = article.find('.entry-content p', first=True).text
    print(summary)

    # vid_src = article.find('iframe', first=True)
    # print(vid_src.html)
    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        # print(vid_src)
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print(yt_link)
    print('-'*40)

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

