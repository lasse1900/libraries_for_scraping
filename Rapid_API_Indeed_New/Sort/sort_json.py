data = [
        {
            "company_logo_url": "https://d2q79iu7y748jz.cloudfront.net/s/_squarelogo/256x256/5a129820b0b27d63b608bd34df1c26f2",
            "company_name": "Scandit",
            "company_rating": "0/5",
            "company_review_link": "No Review Link",
            "company_reviews": 2,
            "date": "23-03-23",
            "job_location": "Tampere",
            "job_title": "Full-stack Engineer - Usage Tracking (Python)",
            "job_url": "https://fi.indeed.com/viewjob?viewtype=embedded&jk=5d2119e1f4d929b4&from=vjs&tk=1gtqnlvtsir0k800&continueUrl=%2Fjobs%3Ffilter%3D0%26q%3D%2527django%2527%26start%3D0%26l%3D%2527tampere%2527",
            "multiple_hiring": "No Multiple Hiring",
            "next_page": "False",
            "page_number": 1,
            "position": 1,
            "salary": "No Salary Mentioned",
            "urgently_hiring": "Not Urgently Hiring"
        },
        {
            "company_logo_url": "No Logo",
            "company_name": "Vaisto Solutions",
            "company_rating": "0/5",
            "company_review_link": "No Review Link",
            "company_reviews": 0,
            "date": "23-05-21",
            "job_location": "Tampere",
            "job_title": "Cloud Software Developer",
            "job_url": "https://fi.indeed.com/viewjob?viewtype=embedded&jk=53f2b15485173fa4&from=vjs&tk=1gtqnm8h62bbp000&continueUrl=%2Fjobs%3Ffilter%3D0%26q%3D%2527python%2Bdeveloper%2527%26start%3D0%26l%3D%2527tampere%2527",
            "multiple_hiring": "No Multiple Hiring",
            "next_page": "True",
            "page_number": 1,
            "position": 1,
            "salary": "No Salary Mentioned",
            "urgently_hiring": "Not Urgently Hiring"
        }
    ]



import json
from datetime import datetime
import re
import math

if __name__ == "__main__":
    temp = sorted(

        data,
        reverse=True,
        key = lambda x: datetime.strptime(x["date"], '%y-%m-%d')
    )

    print(temp)




# from datetime import datetime

# date_string = "21 June, 2018"

# print("date_string =", date_string)
# print("type of date_string =", type(date_string))

# date_object = datetime.strptime(date_string, "%d %B, %Y")

# print("date_object =", date_object)
# print("type of date_object =", type(date_object))

