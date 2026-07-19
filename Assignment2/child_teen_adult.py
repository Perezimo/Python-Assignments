"""Program that determine the ages of child, teen and adult
Enter the age
if age is less than eight years,
print Child
if age is greater than eight and less than eighteen,
print Teen
if age is eighteen and above,
print Adult"""


age = int(input("Enter age:  "))

if (age<8):
	print("You are a Child")

if (age>=8 and age <=17):
	print("You are a Teen")

if (age>=18):
	print("You are an Adult")


