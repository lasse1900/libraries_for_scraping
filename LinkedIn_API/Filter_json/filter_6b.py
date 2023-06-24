import json
import datetime

today = datetime.date.today()
# formatted_date = today.strftime('%d, %m, %y')
# print(formatted_date)
# print(type(formatted_date))
# print(formatted_date)

day, month, year = map(int, today.split('-'))
date_int = year * 10000 + month * 100 + day
print(date_int)
date_int = f"{day}-{month}-{year}"
print(date_int)

# # TODO these date should not be fixed, end date should be today and start date e.g. today - one month
# start_date = datetime.date(2023, 5, 1)
# # end_date = datetime.date(2023, 12, 31)
# int(formatted_date)
# end_date = datetime.date(formatted_date)

# with open('sorted.json') as json_file:
#     data = json.load(json_file)

# filtered_data = [obj for obj in data if start_date <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date]

# # print(filtered_data)

# with open('filtered.json', 'w', encoding='utf-8') as fp:
#     json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)
