class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


e = Employee("Ahmed", 50000, "123-45-6789")
print(e.name)        
print(e._salary)     
# print(e.__ssn)     # raise AttributeError
