"""
program to test if a single character
 entered by the user is a digit
 or character or a special character
"""

single_char = input("Enter a single character:" )

if(single_char.isalpha()):
	print("It is a character:")
elif(single_char.isdigit()):
	print("It's a digit")

else:
	print("It's a special character")