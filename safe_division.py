"""
Safe division of numbers
enter a number X
enter another number Y
if X divided by Y is not equals zero,
print X
if Y is equal zero, 
print "Cannot be divided by zero"
"""

number_1 = int(input("Enter the first number: " ))
 
number_2 = int(input("Enter the second number: " ))


if (number_1 !=0 and number_2 !=0):
	result  = number_1/number_2
	print(result)
else:
	print("Cannot divide by zero")


 

