"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""
file = input("Enter a file name: ")
Split = file.split(".")
filename, filetype = Split
print("File name: "+filename+"\nFile Type: "+filetype)