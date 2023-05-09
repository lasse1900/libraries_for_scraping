import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("HOTMAIL_PASS")

sender = 'lauri.kyttala@hotmail.com'
receiver = 'lauri.kyttala@gmail.com'
password = token

message = """\
Subject: 

This is Lauri!
Just wanted to say hi!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
