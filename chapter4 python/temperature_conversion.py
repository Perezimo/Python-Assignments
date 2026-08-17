

def farenheit(celsius):

    temp_farenheit =(9 / 5) *celsius  + 32

    return temp_farenheit

for celsius in range(0, 101):
    temp_farenheit = farenheit(celsius)
    print("Celsius \t Farenheit")
    print(f"{celsius} \t {temp_farenheit}")
    
