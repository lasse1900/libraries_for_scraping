from reportlab.pdfgen import canvas

c = canvas.Canvas('sample.pdf')
c.drawString(20, 800, 'Merry had a little lamb')
c.drawString(20, 810, 'Merry had a second lamb')
c.save()
