"""program to calculate the largest of three numbers
Enter the first number
Enter the second number
Enter the third number
if first number is greater than the second and the third number,
print the first number as the largest
if the second number is greater than the first and third number,
print the second number is the largest
else, print the third number is the largest"""



first_number= int(input("Enter the first number: " ))
 
second_number = int(input("Enter the second number: " ))

third_number = int(input("Enter the third number: " ))


if (first_number>second_number and first_number>third_number):
	print("The first number is the largest:", first_number)

if (second_number>first_number and second_number>third_number):
	print("The second number is the largest:" , second_number)
else:
	print("The third number is the largest")


 
