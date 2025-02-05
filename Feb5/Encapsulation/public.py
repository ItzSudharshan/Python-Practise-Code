#Public access Modifier
class Demo1:
    def __init__(self, name):
        self.firstname = name
    def dis1(self):
        print(self.firstname)
        
d1 = Demo1('Akash')
print(d1.firstname)
d1.dis1()



class Demo2(Demo1):
    def dis2(self):
        print(self.firstname)
        
d2 = Demo2('Pooja')
print(d2.firstname)
d2.dis1()

        
'''
Rule the Variables which are Public can be accessed
Inside the same class 
Outside the class 
Inside the child class 
Inside Non Child Class

Output :
Akash
Akash
Pooja
Pooja

'''