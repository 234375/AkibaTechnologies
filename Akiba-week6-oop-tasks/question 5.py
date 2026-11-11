# PART A: PRODUCT INFORMATION SYSTEM
class Product:
    store_name = "Akiba Store"
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price, "Birr")
        print("Store:", Product.store_name)

    @classmethod
    def change_store_name(cls, new_name):
        cls.store_name = new_name

    @staticmethod
    def is_valid_price(price):
        return price > 0

product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 800)
print("PRODUCT INFORMATION")
product1.display_product()
print()
product2.display_product()
Product.change_store_name("New Akiba Store")
print("\nAFTER CHANGING STORE NAME")
product1.display_product()

print("\nPRICE VALIDATION")
print("Is 500 valid?", Product.is_valid_price(500))
print("Is -100 valid?", Product.is_valid_price(-100))

class ShoppingCart:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to cart.")

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def display_cart(self):
        print("\nSHOPPING CART")
        for product in self.products:
            print(product.name, "-", product.price, "Birr")
        print("Total:", self.calculate_total(), "Birr")
cart = ShoppingCart()

cart.add_product(product1)
cart.add_product(product2)
cart.display_cart()