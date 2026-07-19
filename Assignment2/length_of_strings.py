"""Program that determines the length of a string
Enter a string to know if it is short string, medium or a long string
if the length of the string is less than 5, 
print short string
if the length of the string greater than 5 and less than equals 10, 
print medium string
if the string length is greater than 10,
print long string
"""

length_of_string = input("Enter a string:")

if (len(length_of_string)<5):
	print("Short string")

if (len(length_of_string)>=5 and len(length_of_string) <=10):
	print("Medium string")


if (len(length_of_string)>=10):
	print("long strings")
