class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


product = Product(100)

print(f"Price: {product.price}")

product.price = 150
print(f"Updated Price: {product.price}")

del product.price
