import json
# JSON data:
# x =  '{ "organization":"GeeksForGeeks", "city":"Noida","country":"India"}'
 
# # python object to be appended
# y = {"pin":110096}
 
# # parsing JSON string:
# z = json.loads(x)
  
# # appending the data
# z.update(y)
 
# # the result is a JSON string:
# print(json.dumps(z))
 
 
import json
 
 
# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
y = {"emp_name":"Simeon",
     "email": "simeon@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
     
write_json(y)

