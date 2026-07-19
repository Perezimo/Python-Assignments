""" Program the calculate the Quadrant of a graph"""


first_integer_X= int(input("Enter the first integer: " ))
 
second_integer_Y = int(input("Enter the second integer: " ))

if ( first_integer_X > 0 and second_integer_Y > 0):
	print("Q1")

if ( first_integer_X < 0 and  second_integer_Y > 0):
	print("Q2")

if ( first_integer_X < 0 and second_integer_Y < 0):
	print("Q3")

if ( first_integer_X > 0 and second_integer_Y < 0):
	print("Q4")

if ( first_integer_X ==0 and second_integer_Y == 0):
	print("Origin")

if ( first_integer_X !=0 and  second_integer_Y == 0):
	print("X-axis")

if ( first_integer_X ==0 and second_integer_Y != 0):
	print("Y-axis")