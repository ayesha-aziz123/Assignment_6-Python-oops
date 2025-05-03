def add_greeting(cls):
    class NewClass(cls):
        def greet(self):
            return "Hello from Decorator!"
    return NewClass

@add_greeting
class Person:
    pass


p = Person()
print(p.greet())  # Output: Hello from Decorator!
