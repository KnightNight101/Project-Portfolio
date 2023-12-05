"""
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module. 
"""
from datetime import date
import calendar
current_date = str(date.today())
dates = current_date.split("-")
print(dates)
# print(calendar.month(current_date[2],current_date[1]))