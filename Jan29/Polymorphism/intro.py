# Duck Typing Example in Python

class Add:
    def calculate(self, a, b):
        print("Addition is:", a + b)

class Sub:
    def calculate(self, a, b):
        print("Subtraction is:", a - b)

# Creating objects
ref_add = Add()
ref_sub = Sub()

# Calling methods using objects
ref_add.calculate(10, 5)  # Output: Addition is: 15
ref_sub.calculate(10, 5)  # Output: Subtraction is: 5

# Duck Typing: The function does not check object type, only behavior
def permit(ref, a, b):
    ref.calculate(a, b)  # Duck Typing: Calls calculate() if the object has it

# Duck Typing: Passing different objects with the same method
permit(Add(), 10, 20)  # Output: Addition is: 30
permit(Sub(), 20, 10)  # Output: Subtraction is: 10

#Ref wont check the type of object 
#ref only gives the importance to the calculate Method