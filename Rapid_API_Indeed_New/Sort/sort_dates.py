# importing datetime
from datetime import datetime

# input list of date strings
inputDateList = ['21-06-14', '23-08-20', '22-04-03']
# inputDateList = ['12-06-14', '01-08-20', '22-04-03']
# inputDateList = ['12-06-2014', '01-08-2020', '22-04-2003', '11-04-2005', '12-10-2002', '23-12-2021']
# inputDateList = ['06-2014', '08-2020', '4-2003', '04-2005', '10-2002', '12-2021']

# sorting the input list by formatting each date using the strptime() function
inputDateList.sort(reverse=True, key=lambda date: datetime.strptime(date, "%y-%m-%d"))

# Printing the input list after sorting
print("The input list of date strings after sorting:\n", inputDateList)