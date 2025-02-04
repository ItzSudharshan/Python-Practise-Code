'''
class Demo1:
    def disp1(Self):
        print('Inside Disp1')
        
class Demo2:
    def disp2(self):
        print('Inside Disp2')
        
d1 = Demo1()
d2 = Demo2()
'''
#Inside Python if we print the reference variable then it will display the string representation  of an Address of an Object '''
#print(d1) #<__main__.Demo1 object at 0x00000195E6D97DA0>
'''
'''
'''
In Python is we print reference variable internally python will invoke the __str__()
which always returns string representation of an address of an object '''
class Demo1:
    def disp1(Self):
        print('Inside Disp1')
    def __str__(self):
        return "Hello!"
        
class Demo2:
    def disp2(self):
        print('Inside Disp2')
    def __str__(self):
        return "Hi"
        
d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)
'''
Output :
Hello!
Hi

In the above examples we have overriden __str__m methods in thier respective Classes.

Dunder Methods: The Methods Which has Suffix and prefix as __(Double Underscore)
These Dunder Methods can be called as Magic Methods because as A programmer we no need to call any method. Automatically methods will be invoked

'''
class Demo1:


    def __str__(self):
        return "Hello!"
        
    def __add__(self, other):
        self.a = 20 
        other.b = 30
        return self.a + other.b
    def __sub__(self, other):
        self.a = 20 
        other.b = 30
        return self.a - other.b
class Demo2:

    def __str__(self):
        return "Hi"
        
d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)
print(d1 + d2)  #50 Output here 
print(d1 - d2)  #Output is -10