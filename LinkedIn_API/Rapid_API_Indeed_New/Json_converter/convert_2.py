import pandoc
text = "Hello world!"
doc = pandoc.read(text)


# paragraph = doc[1][0]
# paragraph

# from pandoc.types import Str
# paragraph[0][2] = Str('Python!')
text = pandoc.write(doc)
print(text)