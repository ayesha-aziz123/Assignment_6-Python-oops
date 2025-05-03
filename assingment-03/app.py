class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} car is starting.")


my_car = Car("Toyota")
print("Car Brand:", my_car.brand)
my_car.start()
