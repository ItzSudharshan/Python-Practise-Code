class GrandParent:
    def __init__(self):
        self.x = 100
        
class Parent(GrandParent):
    def __init__(self):
        super().__init__()  # Corrected the syntax here
        self.y = 200

class Child(Parent):
    def __init__(self):
        super().__init__()  # Corrected the syntax here
        self.z = 300

# Super method is used to invoke the parent
c = Child()
print(c.z)  # Prints 300
print(c.y)  # Prints 200
print(c.x)  # Prints 100


'''
output 
300
200
100

Constructor chaining is the process of calling one constructor from another constructor 
'''