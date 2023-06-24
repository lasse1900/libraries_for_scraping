import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import pandas
from dotenv import load_dotenv
attachments = []

load_dotenv()
email_account = os.environ.get("o365_mail_account")
password = os.environ.get("o365_mail_PASS")

def send_email():
    print("sending emails")
    df = pandas.read_csv('contacts.csv')
    for index, row in df.iterrows():
        sender = "noreply@etteplan.com"
        smtp_server = "smtp.office365.com"
        smtp_port = 587        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg["To"] = row['email']
        name = row['name']
        name_stripped = name.strip()        
        msg['Subject'] = "Open Jobs on Indeed.com"

        body = MIMEText(f"Hello {name_stripped}, here's attached files gererated by AJS-application. \nEmail generated by AJS/Etteplan.")    
        msg.attach(body)    

    # Exception handling if some of files are missing
    try:
        attachments = ['jobs.docx', 'jobs2.docx', 'filtered.json', 'formated.md']

        for attachment_path in attachments:
            with open(attachment_path, "rb") as file:
                attachment = MIMEApplication(file.read())
                attachment.add_header(
                    "Content-Disposition", "attachment", filename=attachment_path
                )
            msg.attach(attachment)
    except Exception as e:
        print("An error occurred while attaching the files", str(e))

    try:
        # Establish a secure connection with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()

            # Log in to the SMTP server, values read from env-variables
            server.login(email_account, password)

            # Send email
            server.send_msg(msg)
        print(f"Email #{index} send!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# Call the function to send the email
send_email()

