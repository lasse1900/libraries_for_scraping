import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("OUTLOOK_PASS")

sender = 'lauri.kyttala@etteplan.com'
receiver = 'lauri.kyttala@gmail.com'
password = token

message = """\
Subject: Hello Hello

This is Lauri!
Just wanted to say hi!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
