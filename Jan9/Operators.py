'''
print(10 // 2) #floor division 
print(True and False)
print(False or True)
print(not True)

A = 1 #ON
B = 0 #OFF
result = A & B
print("Are Both switches ON ?", result)
'''

'''
Operators and Its Types 

What are the different types of operators in Python? 
Answer: Operators in Python are special symbols that perform specific operations on one or more 
operands and return a result.

Python has several types of operators, which can be categorized as :->
1) Arithmetic Operators: These operators perform basic arithmetic operations like addition, 
subtraction, multiplication, division, etc. Suppose you are building a simple calculator 
application. This calculator should be able to add, subtract, multiply, and divide numbers. 
Ex :
a = 10
b = 5

print(a + b) # 15
print(a - b) # 5
print(a * b) # 50
print(a / b) # 2.0


2) 
 Comparison Operators: These operators compare the values of operands and return a 
boolean value (True or False) based on the comparison. 

a = 10 
b = 5

print( a == b) #False
print(a != b) # True 
print(a > b) #True 
print( a < b) #False 



3) Logical Operators: These operators perform logical operations like AND, OR, and NOT. 

Ex: a = True
b = False 

print(a and b) #False
print(a or b) # True 
print(not a ) #False 



4) Assignment Operators: These operators assign values to variables. 
Ex 
a = 10 
a += 5
print(a) #15


5) 
Bitwise Operators: These operators perform bit-level operations on binary numbers. 

a = 5 (0101)
b = 3 ( 0011)

print(a & b) output : 1  (0001)


6) Membership Operators: These operators test for membership in a sequence (e.g., list, tuple, 
string). 

my_list = [1,2,3]
print(1 in my_list) #true 
print(4 not in my_list) #true 



7)  Identity Operators: These operators compare the memory locations of two objects.
a = [1,2,3]
b = a
c = [1,2,3]

print(a is b) # true 
print(a is not c) # false 

'''