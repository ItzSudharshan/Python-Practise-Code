class Demo1:
    def __init__(self, name):
        self.__name = name  #Private Variable 
        
        
        
d1 = Demo1('Akash')

print(d1._Demo1__name)

'''
Output : Akash 

Hence Python Doesnt Support Encapsulation Directly '''
'''
1. Name mangling is the process of Providing new name to the private variable 
2. These new Names will be provided automatically by python for all private members. 
3. New Name will be provided in format: 
objectName._className__variableName
'''