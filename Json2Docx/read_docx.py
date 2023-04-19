import docx

def ReadingTextDocuments(filename):
    doc = docx.Document(filename)

    completedText = []

    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)

    return '\n' .join(completedText)


print(ReadingTextDocuments('test.docx'))