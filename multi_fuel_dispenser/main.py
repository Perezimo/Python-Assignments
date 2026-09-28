from src.dispenser.fuel_dispenser import Dispenser

menu = """
    Welcome to Gbeda Station!
        1. Buy Petroleum
        2. Show Transaction History
    
"""

fuel=[["Petrol", 1300], ["Diesel", 1700], ["Kerosene", 4000], ["Gas", 1600]]
available_petroleum =f"""
        1. {fuel[0][0]} ==> {fuel[0][1]}/liter
        2. {fuel[1][0]} ==> {fuel[1][1]}/liter
        3. {fuel[2][0]} ==> {fuel[2][1]}/liter
        4. {fuel[3][0]} ==> {fuel[3][1]}/liter
"""
operation = True
dispenser = Dispenser()
while operation:
    print(menu)
    option = int(input("Enter option: "))
    if option == 1:
        print(available_petroleum)
        available = int(input("Enter operation: "))
        method = (input("Liter or Amount: "))

        amount = 0
        liter = 0

        if method.lower() == "liter":
            liter = float(input(f"How many Liters of {fuel[available-1][0]} are you buying({fuel[available-1][1]}/L) ?"))
            amount = dispenser.buy_fuel_with_liter(fuel[available-1][0], liter)

        if method.lower() == "amount":
            amount = int(input(f"How much {fuel[available-1][0]} are you buying({fuel[available-1][1]}/L) ?"))
            liter = dispenser.buy_fuel_with_amount(fuel[available-1][0], amount)

        print("Customers Transaction Receipt")
        print("="*40)
        print(f"= \t Product: {fuel[available-1][0]} \t\t\t\t =")
        print(f"= \t Amount: {amount} \t\t\t\t\t =")
        print(f"= \t Liters: {liter} \t\t\t\t\t\t =")
        print(f"= \tThank you for your patronage\t\t=")
        print("="*40)
        print("Saving Transaction History......")

    if option == 2:
        print("All Transactions")
        for product, amount, liters, date in dispenser.check_transaction():
            print("=" * 40)
            print(f"= \t Product: {product} \t\t\t\t =")
            print(f"= \t Amount: {amount} \t\t\t\t\t =")
            print(f"= \t Liters: {liters} \t\t\t\t\t\t =")
            print(f"= \t Date: {date} \t\t\t\t\t\t =")
            print("=" * 40)
            print("")


