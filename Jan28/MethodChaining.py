class GrandParent:
    def cook(self):
        print('Grandparent can cook Birayni')

class Parent(GrandParent):
    def cook(self):
        print("Parent can cook Noodles")

class Child(Parent):
    def cook(self):
        print("Child wont cook")
        super().cook()
        super(Parent, self).cook()
        
c = Child()
c.cook()        
'''
Output 
Child wont cook
Parent can cook Noodles
Grandparent can cook Birayni

method Chaining is the Process of Calling one Method from another method 
'''