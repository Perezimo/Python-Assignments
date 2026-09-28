from datetime import datetime
from xmlrpc.client import DateTime


class Dispenser:
    fuel = {
        "Petrol": [300, 1300],
        "Diesel": [300, 1700],
        "Kerosene": [300, 4000],
        "Gas": [300, 1600],
    }
    transaction = []

    def check_quantity(self, fuel_type):
        if fuel_type in self.fuel:
            return self.fuel[fuel_type][0]
        return "Fuel not available"

    def buy_fuel_with_liter(self, fuel_type, quantity):
        if quantity > 50 or quantity < 1:
            return "Liters must be between 0 and 50"
        if fuel_type in self.fuel:
            if quantity <= self.fuel[fuel_type][0]:
                self.fuel[fuel_type][0] = self.fuel[fuel_type][0] - quantity
                self.save_transaction(fuel_type, self.fuel[fuel_type][1] * quantity, quantity)
                return self.fuel[fuel_type][1] * quantity
        return "Fuel not available"

    def buy_fuel_with_amount(self, fuel_type, amount):
        if fuel_type in self.fuel:
            liter = amount / self.fuel[fuel_type][1]
            self.buy_fuel_with_liter(fuel_type,liter)
            return liter
        return None

    def save_transaction(self,product, amount, liters):
        self.transaction.append((product, amount, liters, datetime.now()))

    def check_transaction(self):
        return self.transaction


    def reset_quantity(self):
        self.fuel["Petrol"][0] = 300
        self.fuel["Diesel"][0] = 300
        self.fuel["Kerosene"][0] = 300
        self.fuel["Gas"][0] = 300
