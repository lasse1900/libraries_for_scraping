
with open('comic.png', 'rb') as rf:
    with open('comic_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)


