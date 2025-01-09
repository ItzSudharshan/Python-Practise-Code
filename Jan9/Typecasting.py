'''a = '30'
b = int(a)
print("Value of a and type of a is ",a, type(a))
print("Value of b and type of b is ",b, type(b))


x = 'Kod'
print(x, type(x))

#y = (int)(x)
#print(y, type(y)) # u will get an error because String to int isnt allowed when u are holding a String value , it should hold an int value 

p = float(input('Enter Float type data'))
print(p, type(p)) # Conversion from float to float is also allowed


'''



'''
#bool
q = 12
print(q, type(q))
q = bool(q)
print(q, type(q))


'''


#TypeCasting 
'''
How does Python handle type conversion between different data types? 
Answers: Typecasting, also known as type conversion, is the process of converting one data type into 
another. Python provides several built-in functions for this. There are two types of type conversion 
in Python: 
1. Implicit Type Conversion: This is done automatically by Python when it's necessary to do so, 
without the programmer's intervention. For instance, if you perform arithmetic operations with 
a mix of int and float values, Python will implicitly convert the int value to a float value. 
2. Explicit Type Conversion: This is done manually by the programmer using predefined functions 
like int(), float(), str(), etc. This is necessary when you want to perform an operation that requires 
a certain type of value, but you have a different type of value. 



'''


'''
print(bool('Kodnest))  #True 
print(int('Kod)) #Error 
print(int('11')) #11
print(float('22.22')) #22.22
print(bool(' ')) #false
print(bool(0)) #False
print(bool(12)) #True 
print(int('12.56')) #Error 
print(int(12.56)) #12








'''