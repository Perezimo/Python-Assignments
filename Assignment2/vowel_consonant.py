"""Program to check if a character entered is a vowel or a consonant
Enter a char
if char is a vowel,
print vowel
else print consonant
"""

letter = input("Enter a letter: ")

if (letter.isalpha()) :
	if (letter =="a" or letter =="e" or letter =="i" or letter=="o" or letter=="u" ):
		print("It is a vowel")
	else:
		print("it is consonant")
else :
	print("Invalid input")
		
