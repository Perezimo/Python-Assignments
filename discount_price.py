def get_item():
	
	name_of_item = input("Enter the name of an item: ")
	original_price = int(input("Enter the original price of the item: "))
	promotional_code = input("Enter the promotional code SAVE10 or HALFOFF of the item: ")
	
	if promotional_code == "SAVE10":
		discount_price = original_price * 0.1
		new_price = original_price - discount_price
		print(new_price)
	elif promotional_code == "HALFOFF":
		discount_price = original_price * 0.5
		new_price = original_price - discount_price
		print(new_price)
	else:
		print("no valid code apply no discount")
		
	return promotional_code

print(get_item())

