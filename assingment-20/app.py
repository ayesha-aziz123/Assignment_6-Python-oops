class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    else:
        print("Age is valid!")

try:
    age = int(input("Enter you age: "))
    check_age(age)

except InvalidAgeError as e:
    print(f"Error: {e}")

except ValueError:
    print("Please enter a valid number.")

