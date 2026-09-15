class Checkout:
    products = []
    def __init__(self):
        pass

    def add_product(self, name, price, quantity):
        self.products.append((name, price, quantity))

    def remove_product(self, name, ):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)

    def remove_products(self):
        self.products.clear()

    def check_cart_quantity(self):
        return len(self.products)

    def check_cart_product_quantity(self, param):
        for product in self.products:
            if product[0] == param:
                return product[2]
        return None

    def check_product_price(self, param):
        for product in self.products:
            if product[0] == param:
                return product[1]
        return None

    def calculate_sub_total(self):
        total = 0
        for product in self.products:
            total += (product[1] * product[2])
        return total

    def calculate_total_per_product(self, param):
        for product in self.products:
            if product[0] == param:
                return product[1] * product[2]
        return None

    def calculate_discount(self, param):
        return self.calculate_sub_total() * param/100

    def calculate_vat(self):
        return self.calculate_sub_total() * 7.5/100

    def calculate_total(self, discount):
        return (self.calculate_sub_total() - self.calculate_discount(discount)) + self.calculate_vat()