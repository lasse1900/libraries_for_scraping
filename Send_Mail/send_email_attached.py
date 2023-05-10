import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("HOTMAIL_PASS")
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = 'lauri.kyttala@hotmail.com'
receiver = 'lauri.kyttala@gmail.com'
password = token

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

body = """
<h2>Hi there!</h2>
Let's hope the attachment arrives!
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

attachment_path = 'jobs.docx'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
message.attach(payload)


server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
# print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()
print("Email send!")