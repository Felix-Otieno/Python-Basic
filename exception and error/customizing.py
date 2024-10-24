class NegativeAgeError(Exception):

    def __init__(self, age, ):
        message = "Age should not be negative"
        self.age = age
        self.message = message

age = int(input("Enter age: "))
if age < 0:
    raise NegativeAgeError(age)
# Output:
# raise NegativeAgeError(age)
# __main__.NegativeAgeError: -9
