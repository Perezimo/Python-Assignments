"""
Program to determine if a number is divisible by 5 and 3
Enter the number
if number modulus 5 is zero and number modulus 3 is zero
print, number is divisible by both 5 and 3"""


number_check = int(input("Enter a number to check if it is divisible by 5 and 3: "))

if (number_check%5 ==0 and number_check%3 == 0):
	print("The number is divisible by 5 and 3:" ,  number_check)

else:
	print("Number not divisible by both numbers")