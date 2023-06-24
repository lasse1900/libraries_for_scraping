import datetime

today = datetime.date.today()
day = today.day
# print(day)

today = datetime.date.today()
month = today.month
# print(month)

today = datetime.date.today()
year = today.year
# print(year)

date_today = f"{day}-{month}-{year}"
print(date_today)

today = datetime.date.today()
year_number = int(today.year % 100)
print(year_number)

date_today = f"{day}-{month}-{year_number}"
print(date_today)

date_today = f"{year}, {month}, {day}"
print(f"date_today  {date_today}")
print(type(date_today))