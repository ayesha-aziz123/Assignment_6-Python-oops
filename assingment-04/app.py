class Bank:
    bank_name = "Meezan Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")


# Creating instances
customer1 = Bank("Alice")
customer2 = Bank("Bob")

# Display before changing bank name
customer1.display()
customer2.display()

# Changing bank name using class method
Bank.change_bank_name("New Future Bank")

# Display after changing bank name
customer1.display()
customer2.display()
