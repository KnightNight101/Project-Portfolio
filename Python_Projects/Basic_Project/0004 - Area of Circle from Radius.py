"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math
UserInput = float(input("Enter a radius in mm to get the area of the circle with that radius: "))
Area = math.pi*UserInput*UserInput
print("The Area of the circle is: "+str(Area)+"mm^2")
