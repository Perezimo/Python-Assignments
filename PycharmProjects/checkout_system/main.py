from datetime import datetime
from xmlrpc.client import DateTime

from src.checkout.checkout import Checkout

check_out = Checkout()
name = input("What is the customer's name? ")
choice = True
while choice:
    item = input("What did the user buy? ")
    quantity = int(input("How many pieces? "))
    price = float(input("How much per unit? "))
    check_out.add_product(item, quantity, price)
    more = input("Add more items? (yes/no): ").strip().lower()
    if more == "no":
        choice = False
    if more == "yes":
        continue
cashier_name = input("What is your name? ")
discount = float(input("How much discount will he get? "))

print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312 HERBERT MACAULAY WAY, SABO, YABA""")
print("Tel: 03293828342")
print("Date: " + datetime.now().strftime("%d-%b-%Y %I:%M %p") + "\nCashier: " + cashier_name + "\nCustomer Name: " + name)
print("=" * 100)
print("-"*100)
for product in check_out.products:
    print(f"\t{product[0]} \t{product[2]} \t{product[1]} \t{check_out.calculate_total_per_product(product[0])}")

print("\t\tSub Total:\t" + str(check_out.calculate_sub_total()) + "\n\t\tDiscount:\t" + str(check_out.calculate_discount(discount)) + "\n\t\tVAT@7.5:\t" + str(check_out.calculate_vat()))
print("="*100)
print("\t\tBill Total:\t" + str(check_out.calculate_total(discount)))
print("="*100)
print("THIS IS NOT A RECEIPT, KINDLY PAY " + str(check_out.calculate_total(discount)))
amount = input("How much did the customer give to you?")

print("Amount Paid: " + str(amount))
balance = float(amount) - check_out.calculate_total(discount)
print("Balance: " + str(balance))
print("="*100)
print("THANKS FOR YOUR PATRONAGE")
print("="*100)