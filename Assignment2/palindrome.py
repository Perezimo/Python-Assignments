"""
Program that check a work if it is
a palindrome or not
Enter a word
if the word is a palindrome,
print"yes, it is a palindrome
e;se, print not a palindrome"""


word = input("Enter a word:" )

if(word.is_palindrome()):
	print("This is a palindrome:")

else:
	print("This is not a palindrome:")

