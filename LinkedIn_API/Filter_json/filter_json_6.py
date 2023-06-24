import json
import datetime
from dateutil.relativedelta import relativedelta

today = datetime.date.today()
# Format the month with a single digit when needed
month_str = str(today.month) if today.month >= 10 else "" + str(today.month)
formatted_date = f"{today.day},{month_str},{today.year%1000}"
print(type(formatted_date))
PVM_LÄHDE = formatted_date
print(f"PVM_LÄHDE {PVM_LÄHDE}")

def filter():
    end_date = datetime.datetime.strptime(PVM_LÄHDE, '%d,%m,%y')
    print(end_date)
    end_date2 = end_date.strftime("%d,%m,%y")
    print(end_date2)
    end_date_object = datetime.datetime.strptime(end_date2, "%d,%m,%y").date()
    print(f"date_object {end_date_object}")
    print(type(end_date_object))

    start_date = end_date - relativedelta(months=1)
    print(start_date)
    start_date2 = start_date.strftime("%d,%m,%y")
    print(start_date2)
    start_date_object = datetime.datetime.strptime(start_date2, "%d,%m,%y").date()    
    print(f"date_object {start_date_object}")
    print(type(start_date_object))

    with open('sorted.json') as json_file:
        data = json.load(json_file)

    filtered_data = [obj for obj in data if start_date_object <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date_object]

    with open('filtered.json', 'w', encoding='utf-8') as fp:
        json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)

if __name__ == '__main__':
    filter()