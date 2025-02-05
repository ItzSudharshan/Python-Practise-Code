class Demo1:
    def __init__(self, name):
        self.__name = name  #Private Variable 
    
    def getName(self):
        return self.__name
    
    def setName(self, newName):
        self.__name = newName
        
        
        
        
d1 = Demo1('Akash')
print(d1.getName()) 


'''
Output 
Akash
'''
d1.setName('Priya')
print(d1.getName())

'''
Direct access not Allowed so we used getter and setter method . Therefore the output for the above code is as folows
Akash
Priya
'''