"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
from datetime import date
from datetime import datetime

current_date = date.today()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print(current_date+"\n"+current_time)

