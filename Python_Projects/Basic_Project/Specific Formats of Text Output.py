"""Write a Python program to print the following string in a specific format (see the output).
Sample String: 
Twinkle, twinkle, little star, 
    How I wonder what you are! 
        Up above the world so high, 
        Like a diamond in the sky. 
    Twinkle, twinkle, little star, 
How I wonder what you are
"""
# Trial 1

"""
line1 = "Twinkle, twinkle, little star,"
line2 = "   How I wonder what you are!"
line3 = "       Up above the world so high,"
line4 = "       Like a diamond in the sky."
line5 = "   Twinkle, twinkle, little star"
line6 = "How I wonder what you are"

print(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6)
"""

# The solution as provided
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
# Updating my code with the \t command

a, b, c, d = "Twinkle, twinkle, little star," , "How I wonder what you are!","Up above the world so high," ,"Like a diamond in the sky."
print(a+"\n\t"+b+"\n\t\t"+c+"\n\t\t"+d+"\n\t"+a+"\n"+b)


