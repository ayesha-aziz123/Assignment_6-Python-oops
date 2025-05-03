class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting...")

class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine  

    def start_car(self):
        print(f"Starting {self.make} car.")
        self.engine.start()  

engine1 = Engine(250)
car1 = Car("Ford", engine1)

car1.start_car()
