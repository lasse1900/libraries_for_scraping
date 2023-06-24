import json
import datetime
from dateutil.relativedelta import relativedelta
PVM_LÄHDE = '1-5-23'

def filter():
    today = datetime.date.today()
    formatted_date = today.strftime('%d-%m-%y')
    print(f"Date today is: {formatted_date} is short format (same as in json files)")

    # TODO these date should not be fixed, end date should be today and start date e.g. today - one month
    # start_date = datetime.date(2023, 4, 1)
    # end_date = datetime.date(2025, 12, 31)
    end_date = datetime.datetime.strptime(PVM_LÄHDE, '%d-%m-%y')
    print(end_date)
    end_date2 = end_date.strftime("%d-%m-%y")
    print(end_date2)
    date_object = datetime.datetime.strptime(end_date2, "%d-%m-%y").date()
    print(f"date_object {date_object}")

    start_date = end_date - relativedelta(months=1)
    print(start_date)
    start_date2 = start_date.strftime("%d-%m-%y")
    print(start_date2)
    print(type(start_date2))

    # with open('sorted.json') as json_file:
    #     data = json.load(json_file)

    # filtered_data = [obj for obj in data if start_date2 <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date2]

    # with open('filtered.json', 'w', encoding='utf-8') as fp:
    #     json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)

if __name__ == '__main__':
    filter()