# import datetime

# today = datetime.date.today()
# day = today.day
# day = int(today.day % 10)
# month = today.month
# year = int(today.year % 100)
# year = today.year

# date_today = f"{day}-{month}-{year}"
# date_today = f"{year}-{month}-{day}"
# print(date_today)
# print(type(date_today))

import datetime

CONSTANT_DATE = datetime.date(2023, 12, 31)

# Accessing the constant date's components
year = CONSTANT_DATE.year
month = CONSTANT_DATE.month
day = CONSTANT_DATE.day

# Printing the constant date's components
print(year)
print(month)
print(day)
