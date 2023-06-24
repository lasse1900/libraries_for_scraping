import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("ETTEPLAN_PASS")

from email.mime.text import MIMEText

msg = MIMEText("Hello, this is a test email.")
msg["Subject"] = "AJS Open Jobs"
msg["From"] = "noreply@etteplan.com"
msg["To"] = "lauri.kyttala@gmail.com"

server = smtplib.SMTP("82.195.202.152", 25)  # Replace with the actual server address and port

server.sendmail("noreply@etteplan.com", "lauri.kyttala@gmail.com", msg.as_string())
server.sendmail("noreply@etteplan.com", "lauri.kyttala@etteplan.com", msg.as_string())

server.quit()

print("Emails send!")
