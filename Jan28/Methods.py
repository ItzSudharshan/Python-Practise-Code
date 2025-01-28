class Student:
    def cook(self):
        print('Student is Cooking')
    def play(self):
        print('Playing Cricket')
        
class Employee(Student):
    def work(self):
        print('Employee is Working')
    def cook(self):
        print('Employee is Cooking')
        
        
e = Employee()
e.play()
    
'''
Output 
Inherited Method 
Playing Cricket

Work() : specialized Method  Only in Child Class 
play() : Inherited Method  Used as it is present in Child class 
cook() : Overriden Method Change Implementation in Child Class 

'''