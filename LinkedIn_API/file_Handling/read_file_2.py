import yagmail
import os
import pandas
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("YAGMAIL_PASS")
from datetime import datetime as dt
today = dt.today()

# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list


# with open("my_terms_1.txt") as file:
#     lines = [line.rstrip() for line in file]
#     print(lines[0])
#     print(lines[1])


# def read_file():
#     df = pandas.read_csv('my_terms.csv')
#     for index, row in df.iterrows():
#         contents = [{row['keyword'], row['location']}]
#         print(contents[0])
#         contents = [f"""
#             Hi {row['keyword']}, here's attached the daily fi.indeed.com open jobs listing! 
#             """,row['location'],
#         ]
#         print(row['keyword'])


sender = 'lauri.kyttala@gmail.com'
subject = "Open Jobs on Indeed - " + today.strftime("%B %d, %Y")

# def send_email():
yag = yagmail.SMTP(user=sender, password=token)
df = pandas.read_csv('contacts.csv')
for index, row in df.iterrows():
    contents = [f"""
        Hi {row['name']}, here's attached the daily fi.indeed.com open jobs listing! 
        """,row['filepath'],
    ]
    # print(row['email'])
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("emails sent!")