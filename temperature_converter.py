def get_temperature():
	temperature= int(input("Enter temperature in celsius:"))
	temperature_farenheit = temperature *9/5 + 32	
	
	if temperature_farenheit <=50:
			print("Cold advisory")
	if temperature_farenheit >50:
			print("Heat alert")

	return temperature_farenheit

print(get_temperature())
		
		