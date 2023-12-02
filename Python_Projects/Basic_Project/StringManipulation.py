"""
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. 
"""
print("Hello! This program converts a first name and last name and prints them in reverse! \n")
input = input("Please write your first and last name with a space inbetween!: ")
reverse_input = input[::-1]
print(reverse_input+ "\n")
sliced_input = input.split()
first,last = sliced_input
print("First name: " + first + "\n")
print("Last name: " + last + "\n")
print("Reversed: " + last +" "+ first)
