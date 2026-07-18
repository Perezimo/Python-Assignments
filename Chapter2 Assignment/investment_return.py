"""Exercise2.12. Investment return.
Enter principal amount
get annual interest rate
get number of years
Total amount after 10, 20 and 30 years is
total_amount = p(1+r) to the power of n

print amount in the first 10years
print amount in 20years
get amount in 30years
"""

principal_amount = 10000

interest_rate = 7/100

amount_first_10years = principal_amount *( 1 + 7/100)**10

amount_20years = amount_first_10years *( 1 + 7/100)**20

amount_30years = amount_20years*( 1 + 7/100)**30

print("The Amount for the first 10 yeras is:", amount_first_10years)

print("The Amount for 20years is:" , amount_20years)

print("The Amount for 30years is:" , amount_30years)



