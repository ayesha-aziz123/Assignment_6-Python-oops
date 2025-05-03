class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

m = Multiplier(3)
print(callable(m))
print(m(10))