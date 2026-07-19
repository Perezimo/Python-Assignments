"""Greetings based the length of strings
"""

name = input("Enter your name to know the type of greetings you deserved:")

if(len(name)<5):
	print("You deserve a short greetings:" , "Hi" , name)

else: 
	print("You deserve a long greetings:" , "Hello" , name)

