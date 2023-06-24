from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("HOTMAIL_PASS")

sender = "lauri.kyttala@outlook.com"
recipient = "lauri.kyttala@gmail.com"
message = "Hello world!"

email = EmailMessage()
email["From"] = sender
email["To"] = recipient
email["Subject"] = "Test Email from Matti's example"
email.set_content(message)

smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(sender, token)
smtp.sendmail(sender, recipient, email.as_string())
smtp.quit()