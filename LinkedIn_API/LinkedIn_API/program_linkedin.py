from linkedin_api import Linkedin
import json
from jsonformatter import JsonFormatter
from jsonformatter import basicConfig
import ast
import pprint
import json


# https://www.youtube.com/watch?v=zsncS1gqanM

api = Linkedin('lauri.kyttala@gmail.com','TAmmiholma8')
decision = input('A) Get profile from username\nB) Search School\nC) Search for people\nD) Search for Company:\n')
print('Your decision is', str(decision))
if decision == 'A' or decision == 'a':
    username = input('Input the username you want to search: ')
    print(api.get_profile(username))
elif decision == 'B' or decision == 'b':
    school = input('Input school keyword: ')
    print(api.get_school(school))
elif decision == 'C' or decision == 'c':
    people = input('Input keyword for searching people: ')
    print(api.search_people(people))
elif decision == 'D' or decision == 'd':
    company = input('Input company name: ')
    # print(api.get_company(company))
    input_list = ['']
    input_list.append(api.get_company((company)))
    input_out = json.dumps(input_list)
 
    # print(json.dumps(input_list))

    # https://stackoverflow.com/questions/67475333/typeerror-write-argument-must-be-str-not-dict-python
    # print(input_out)
    for x in range(len(input_list)):
        outfile = open('logfile_abb.log', 'w')
        print((input_list[x]), file=outfile)
        outfile.close()


# print(json.dumps(api.get_profile(username)))
