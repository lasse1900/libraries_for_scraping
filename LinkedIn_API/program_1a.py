from linkedin_api import Linkedin
import json
# https://www.youtube.com/watch?v=zsncS1gqanM

api = Linkedin('lauri.kyttala@gmail.com','TAmmiholma8')
username = input('Input the username you want to search: ')
print(api.get_profile(username))

# print(json.dumps(api.get_profile(username)))
# api.search()