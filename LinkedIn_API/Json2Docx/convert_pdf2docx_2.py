from collections.abc import Iterable

from pdf2docx import Converter

# source_file
pdf_file = 'python.pdf'

# output file
docx_file = 'output.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()