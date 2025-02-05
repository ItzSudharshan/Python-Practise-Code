#Protected access Modifier
class Demo1:
    def __init__(self, name):
        self._firstname = name #protected 
    def dis1(self):
        print(self._firstname)
        
d1 = Demo1('Akash')
print(d1._firstname)
d1.dis1()



class Demo2(Demo1):
    def dis2(self):
        print(self._firstname)
        
d2 = Demo2('Pooja')
print(d2._firstname)
d2.dis1()

class Demo3:
    def disp3(self):
        print(d1._firstname)
        
d3 = Demo3()
d3.disp3()
'''
Otput :
Akash
Akash
Pooja
Pooja
Akash

Rule the Variables which are Protected can be accessed
Inside the same class 
Outside the class 
Inside the child class 
Inside Non Child Class


Therefore Consusion is same as Public, Since python is isnt Strict 

The variables which are protected should be accessed inside the same class and inside the child class and this is 
programmers duty to follow this rules


'''