#In this code we are achieving Polymorphsim using Method Overrinding
# Base class
class Calculator:
    def calculate(self, a, b):
        print("Performing calculation...")

# Derived class for addition
class Add(Calculator):
    def calculate(self, a, b):  # Overriding the base class method
        print("Addition is:", a + b)

# Derived class for subtraction
class Sub(Calculator):
    def calculate(self, a, b):  # Overriding the base class method
        print("Subtraction is:", a - b)

# Creating objects of derived classes
ref_add = Add()
ref_sub = Sub()

# Calling overridden methods directly
ref_add.calculate(10, 5)  # Output: Addition is: 15
ref_sub.calculate(10, 5)  # Output: Subtraction is: 5
