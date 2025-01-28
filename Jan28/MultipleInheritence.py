'''
class Demo1:
    def disp1(self):
        print('Inside Disp1')
        
class Demo2:
    def disp2(self):
        print('Inside Disp2')
        
class Demo3(Demo1, Demo2):
    pass

d3 = Demo3()
d3.disp1()
d3.disp2()
#d3.disp()
Output :
Inside Disp1
Inside Disp2

'''

class Demo1:
    def __init__(self):
        self.x = 100

class Demo2:
    def __init__(self):
        self.x = 200

class Demo3(Demo2, Demo1):
    def __init__(self):
        self.x = 300
        
d3 = Demo3()
print(d3.x)
        
#Output -> 300  Constructs arent inherited if your child has been assigned a value 
'''
constructors are not inherited in Python. When you create a subclass, the constructor of the parent class is not automatically called. You'll need to call it explicitly using super() if you want to use the parent class's constructor in the subclass.
'''