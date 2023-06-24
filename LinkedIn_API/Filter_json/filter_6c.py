import json
import datetime
from dateutil.relativedelta import relativedelta

today = datetime.date.today()
day = today.day
day = int(today.day % 10)
month = today.month
year = int(today.year % 100)
year = today.year

# date_today = f"{day}-{month}-{year}"
date_today = f"{year}, {month}, {day}"
print(f"date_today  {date_today}")
print(type(date_today))

today = datetime.date.today()
formatted_date = today.strftime('%d-%m-%y')
print(formatted_date)

# ------------------//------------------
today = datetime.date.today()
one_month_ago = today - relativedelta(months=1)
print(f"Month ago: {one_month_ago}")


# start_date = "2023, 4, 1"
start_date = "2023, 4, 1"
# TODO these date should not be fixed, end date should be today and start date e.g. today - one month
start_date = datetime.date(2023, 4, 1)
# start_date = datetime.date(one_month_ago)
end_date = datetime.date(2023, 12, 31)
# end_date = datetime.date(date_today)

with open('sorted.json') as json_file:
    data = json.load(json_file)

# filtered_data = [obj for obj in data if start_date <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date]
filtered_data = [obj for obj in data if start_date <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date]

# print(filtered_data)

with open('filtered.json', 'w', encoding='utf-8') as fp:
    json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)


# ------------------------
print('--------------***---------------')

def datetime_to_int(dt):
    pvm = int(dt.strftime("%Y%m%d"))
    # pvm = int(dt.strftime("%Y%m%d%H%M%S"))
    print(type(pvm))
    return pvm


print(datetime_to_int(today))

# df.Date = df.Date.str.replace('-', '').astype(int)



