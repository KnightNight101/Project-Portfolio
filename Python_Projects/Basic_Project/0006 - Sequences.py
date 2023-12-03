"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
# Information about Lists and Tuples
"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data: 3, 5, 7, 23
Python list:
    A list is a container which holds comma separated values (items or elements) 
    between square brackets where items or elements need not all have the same type. 
    In general, we can define a list as an object that contains multiple data items (elements). 
    The contents of a list can be changed during program execution. 
    The size of a list can also change during execution, as elements are added or removed from it.
Python tuple:
    A tuple is container which holds a series of comma separated values (items or elements) 
    between parentheses such as an (x, y) co-ordinate. 
    Tuples are like lists, except they are immutable 
    (i.e. you cannot change its content once created) and can hold mix data types.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
input = input("This is program that accepts a sequence of comma-separated numbers from you and generates a list and a tuple of those numbers: ")
slicenumbers = input.split(",")
a,b,c,d = slicenumbers
print(a + "\n" + b + "\n" + c + "\n" + d)