"""Ticket price calculator
Enter the age of user
if the age of user is less than or 5years, 
print free ticket
if the age of the user is greater than 5years and less than 13years
print ticket price of $5
if the age of the user is more than 13years and less than 65years
print ticket price is $12
if the age of the user is more than 64years,
print ticket as $8.
"""



age = int(input("Enter your age:"))

if(age <= 5):
	print("Free ticket")

if(age > 5 and age <= 12):
	print("Your ticket is: $5")

if(age > 13 and age <= 64):
	print("Your ticket is: $12")

if(age > 65):
	print("Your ticket is: $8")

