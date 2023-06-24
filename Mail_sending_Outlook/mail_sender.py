import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
    body = "Test SMTP Service from Python on Port 587"
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
