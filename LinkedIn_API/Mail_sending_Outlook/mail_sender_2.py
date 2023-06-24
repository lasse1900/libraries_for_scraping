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
    sender_email = "noreply@etteplan.com"
    receiver_email = "lauri.kyttala@etteplan.com"
    subject = "smtprelay Test Email"
    body = "Here's attached files gererated by AJS-application."
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    # Get user credentials
    sender_username = email_account
    sender_password = password

    # Create message object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Add email body
    body = MIMEText("Here's attached files gererated by AJS-application.")
    message.attach(body)

    # # Add attachments to be send the list below
    attachments = ['jobs.docx', 'jobs2.docx', 'filtered.json', 'formated.md']

    for attachment_path in attachments:
        with open(attachment_path, "rb") as file:
            attachment = MIMEApplication(file.read())
            attachment.add_header(
                "Content-Disposition", "attachment", filename=attachment_path
            )
        message.attach(attachment)    

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
