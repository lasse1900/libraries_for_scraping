from docx import Document
from docx.enum.dml import MSO_THEME_COLOR_INDEX
from docx.shared import Pt

# Create a new document
doc = Document()

# Add a paragraph with a hyperlink
paragraph = doc.add_paragraph()
hyperlink = paragraph.add_hyperlink("http://www.example.com", "Example Hyperlink")
hyperlink.style = "Hyperlink"
hyperlink.font.color.rgb = MSO_THEME_COLOR_INDEX.HYPERLINK
hyperlink.font.underline = True

# Save the document
doc.save("output.docx")
