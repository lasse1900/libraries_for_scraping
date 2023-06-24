import json

json_data = """[
    {
        "company_logo_url": "https://d2q79iu7y748jz.cloudfront.net/s/_squarelogo/256x256/5a129820b0b27d63b608bd34df1c26f2",
        "company_name": "Scandit",
        "company_rating": "0/5",
        "company_review_link": "No Review Link",
        "company_reviews": 2,
        "date": "15-03-23",
        "job_location": "Tampere",
        "job_title": "Full-stack Engineer - Usage Tracking (Python)",
        "job_url": "https://fi.indeed.com/viewjob?viewtype=embedded&jk=5d2119e1f4d929b4&from=vjs&tk=1gtqnlvtsir0k800&continueUrl=%2Fjobs%3Ffilter%3D0%26q%3D%2527django%2527%26start%3D0%26l%3D%2527tampere%2527",
        "multiple_hiring": "No Multiple Hiring",
        "next_page": "False",
        "page_number": 1,
        "position": 1,
        "salary": "No Salary Mentioned",
        "urgently_hiring": "Not Urgently Hiring"
    }
]"""

print(json_data)

content = json.loads(json_data)[0]
print(type(content))
print(content)


def format(key, value):
    return f"<{value}>" if key.endswith("_url") else value


for key, value in content.items():
    print(f"- {key} : {format(key, value)}")