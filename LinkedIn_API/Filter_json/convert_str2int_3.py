import datetime

date_string = '12-05-23'
# date_object = datetime.datetime.strptime(date_string, '%d-%m-%y').date()
# print(date_object)
# print(type(date_object))

# print(date_object)

day, month, year = map(int, date_string.split('-'))
date_int = year * 10000 + month * 100 + day
print(date_int)
date_int = f"{day}-{month}-{year}"
print(date_int)

