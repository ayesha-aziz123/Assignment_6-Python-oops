class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  

    def show_details(self):
        print(f"Department: {self.department_name}, Employee: {self.employee.name}")


emp1 = Employee("Alice")  
dept1 = Department("HR", emp1)  

dept1.show_details()
