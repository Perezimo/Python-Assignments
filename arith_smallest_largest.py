"""
Exercise 2.10
"""
first_number = int(input("Enter the first number:  "))

second_number = int(input("Enter the first number:  "))

third_number = int(input("Enter the first number:  "))

sum = first_number + second_number + third_number
print("The sum of the numbers is:" , sum)

average = sum/3
print("The average is:" , average)

product = first_number*second_number*third_number
print("The products of the number is:" , product)


if first_number>second_number and first_number >third_number:
	print("The largest number is" , first_number)


if first_number<second_number and first_number<third_number:

	print("The smallest number is" , first_number)


if second_number>first_number and second_number>third_number:
	print("The largest number is" , second_number)

if second_number<first_number and second_number<third_number:

	print("The smallest number is" , second_number)

if third_number>first_number and third_number >second_number:
	print("The largest number is" , third_number)

if third_number<second_number and third_number<first_number:
	print("The smalles number is" , third_number)









