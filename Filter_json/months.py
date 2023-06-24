import datetime

today = datetime.date.today()

# Format the month with a single digit when needed
month_str = str(today.month) if today.month >= 10 else "" + str(today.month)

formatted_date = f"{today.day},{month_str},{today.year%1000}"
print(type(formatted_date))
print("Day today", formatted_date)
