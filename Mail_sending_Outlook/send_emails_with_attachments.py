import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv
attachments = []

load_dotenv()
email_account = os.environ.get("o365_mail_account")
password = os.environ.get("o365_mail_PASS")

def send_email():

    sender = "noreply@etteplan.com"
    receiver = "lauri.kyttala@gmail.com"
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = "Open Jobs on Indeed.com"

    body = """
    <h2>Hi, here's attached files gererated by AJS-application!</h2>

    Br, AJS-team
    """
    mimetext = MIMEText(body, 'html')
    message.attach(mimetext)

    # Exception handling if some of files are missing
    try:
        attachments = ['jobs.docx', 'jobs2.docx', 'filtered.json', 'formated.md']

        for attachment_path in attachments:
            with open(attachment_path, "rb") as file:
                attachment = MIMEApplication(file.read())
                attachment.add_header(
                    "Content-Disposition", "attachment", filename=attachment_path
                )
            message.attach(attachment)
    except Exception as e:
        print("An error occurred while attaching the files", str(e))

    try:
        # Establish a secure connection with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()

            # Log in to the SMTP server, values read from env-variables
            server.login(email_account, password)

            # Send email
            server.send_message(message)

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# Call the function to send the email
send_email()

