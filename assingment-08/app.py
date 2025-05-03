class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject
        print(f"Teacher constructor called, Subject: {self.subject}")

    def show_info(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

t1 = Teacher("Maryam", "Biology")
t2 = Teacher("Asma", "CS")

t1.show_info()
t2.show_info()

