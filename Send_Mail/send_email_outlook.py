import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("OUTLOOK_PASS")

# Outlook SMTP server settings
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
# smtp_username = 'your_email@example.com'
smtp_username = 'lauri.kyttala@etteplan.com'
smtp_password = token

sender = 'lauri.kyttala@etteplan.com'
recipient = 'lauri.kyttala@gmail.com'
subject = 'Test Email'
message = 'This is a test email sent via Outlook SMTP.'

# Create the email message
email = MIMEMultipart()
email['From'] = sender
email['To'] = recipient
email['Subject'] = subject

email.attach(MIMEText(message, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender, recipient, email.as_string())
    print("Email sent successfully!")

except Exception as e:
    print("An error occurred while sending the email:", str(e))

finally:
    # Disconnect from the server
    server.quit()
