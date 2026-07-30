def is_palindrome(number):
	if number < 10:
		print("number must be more than a digit")
		return
	keep_number = str(number)
	new_number =""
	for _ in range(0,len(keep_number)):
		new_number+=str(number%10)
		number//=10
	if keep_number == new_number:
		return True
	else:
		return False
		


def is_prime(number):
	for count in range(2,number//2 + 1):
		if number%count == 0:
			return False

	return True
	

def is_palindrome_prime(number):
	if is_palindrome(number) and is_prime(number):
		return True
	else:
		return False


number=int(input("Enter a number to check if it is palindrome and prime: "))
print(is_palindrome_prime(number))