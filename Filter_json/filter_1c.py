import csv
import json
import datetime

# Lue päivämäärä CSV-tiedostosta
with open('dates.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Ohita otsikkorivi
    day, month, year = map(int, next(reader))  # Lue ensimmäinen data-rivi
    print(day, month, year)

# Muunna päivämäärä datetime-objektiksi
desired_date = datetime.datetime(day, month, year)
print(desired_date)

with open('short2.json') as json_file:
    data = json.load(json_file)

# Filter objects based on date JSON format is: [{"date": "11-04-23"}],
# filtered_objects = [obj for obj in data if datetime.datetime.strptime(obj['date'], '%Y-%m-%d') > desired_date]
filtered_objects = [obj for obj in data if datetime.datetime.strptime(obj['date'], '%d,%m,%y') <= desired_date]

# print(filtered_objects)

with open('filtered.json', 'w', encoding='utf-8') as fp:
    json.dump(filtered_objects, fp, indent=2, ensure_ascii=False, sort_keys=True)