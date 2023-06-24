import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
attachments = []

load_dotenv()
email_account = os.environ.get("o365_mail_account")
password = os.environ.get("o365_mail_PASS")

def send_email():

    sender = "noreply@etteplan.com"
    receiver = "lauri.kyttala@etteplan.com"
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    # Get user credentials
    sender_username = email_account
    sender_password = password

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Hello again!'

    body = """
    <h2>Hi, here's attached files gererated by AJS-application!</h2>

    Br, AJS-team
    """
    mimetext = MIMEText(body, 'html')
    message.attach(mimetext)

    attachment_path = 'jobs2.docx'
    attachment_file = open(attachment_path, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload(attachment_file.read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
    message.attach(payload)

    try:
        # Establish a secure connection with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()

            # Log in to the SMTP server
            server.login(sender_username, sender_password)

            # Send email
            server.send_message(message)

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# Call the function to send the email
send_email()

