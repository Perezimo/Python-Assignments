"""Program that calculate the cost of a trip.

Enter the distance.
Enter the fuel efficiency of the car in miles per gallon
Enter price of fuel per gallon
Calculate the cost of the trip.
cost of trip is distance covered divided 
by car efficiency multiplied by cost of fuel
"""

distance_covered = int(input("Enter the distance in miles: "))

car_efficiency = int(input("Enter the fuel efficiency of the car: "))

price_fuel = int(input("Enter the cos per gallaon of fuel: $"))

cost_of_trip = (distance_covered/car_efficiency)* price_fuel

print("The cost of the trip is:$", cost_of_trip)

