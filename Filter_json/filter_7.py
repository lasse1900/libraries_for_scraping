import json
import datetime
from dateutil.relativedelta import relativedelta

# Dates formated alined with json dates: "date": "11-05-23"
today = datetime.date.today()
print(today)
formatted_date = today.strftime('%d-%m-%y')
one_month_ago = today - relativedelta(months=1)
formatted_date_one_month_ago = one_month_ago.strftime('%d-%m-%y')

# end date should be today's date, start date e.g. one month ago
# start_date = datetime.date(formatted_date_one_month_ago) # date one month ago
# end_date = datetime.date(formatted_date) # today's date

start_date = datetime.date(1-4-23)
end_date = datetime.date(12-5-23)
# end_date = datetime.date(formatted_date) # today's date

with open('sorted.json') as json_file:
    data = json.load(json_file)

filtered_data = [obj for obj in data if start_date <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date]

# print(filtered_data)

with open('filtered.json', 'w', encoding='utf-8') as fp:
    json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)

# ------------------------------------

# import datetime
# from dateutil.relativedelta import relativedelta

# today = datetime.date.today()
# one_month_ago = today - relativedelta(months=1)
# print(one_month_ago)
