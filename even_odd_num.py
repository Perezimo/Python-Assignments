"""Execise 2.6
Prompt the user for a number
if the remainder of the number when divided by 2 is zero,
print number is an even number. 
else, print "number is an odd number.
"""



number =int (input("Enter a number:  "))

if number%2 ==0:
	print("The number is even:" , number)

else:
	print("The number is odd:"  , number)