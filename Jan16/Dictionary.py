'''
What is a Dictionary?

A dictionary in Python is a collection of key-value pairs. It’s like a real dictionary where you look up a word (the key), and you get its definition (the value). Each key in a Python dictionary must be unique, but the values don’t have to be.


'''
d1  = {
    'name' : 'Sudharshan Nayak',
    'age' : 25,
    'Phone' : 7892
}
print(d1, type(d1)) #{'name': 'Sudharshan Nayak', 'age': 25, 'Phone': 7892} <class 'dict'>

d1['name'] = 'Vineeth'
print(d1)  #{'name': 'Vineeth', 'age': 25, 'Phone': 7892} 

'''
1) In Dict We cannot store Duplicate Keys 
2) In Dict We can store Duplicate Values
3) Dict are Mutable 




'''

for i in d1.keys():  #Keys will be Displayed
    print(i)
    
    
for i in d1.values():  #Values are Displayed 
    print(i)
    
for i in d1.items():  #Key and Values are Displayed 
    print(i)
    
    
#We have lsit(), tuple(), set() and Dict() These are typically used in Type Casting Files


#Creating a Dictionary 
student = {
    'name': 'Amit',
    'age': 21,
    'course': 'Computer Science'
}
print(student)  #{'name': 'Amit', 'age': 21, 'course': 'Computer Science'}

#----------------------------------------------------------------------------
#Accessing Values in a Dictionary

print(student['name']) #Amit

#---------------------------------------------------------------------------
#Adding and Updating Values
student['grade'] = 'A'
print(student)  #{'name': 'Amit', 'age': 21, 'course': 'Computer Science', 'grade': 'A'}

#Updating an Existing Value
student['age'] = 22
print(student)  #{'name': 'Amit', 'age': 22, 'course': 'Computer Science', 'grade': 'A'}

#-------------------------------------------------------------------------------------------
#Removing Items from a Dictionary

del student['grade']
print(student)  #{'name': 'Amit', 'age': 22, 'course': 'Computer Science'}

#---------------------------------------------------------------------------------------------

#Using .pop() to Remove a Key-Value Pair
course = student.pop('course')
print(student)    #{'name': 'Amit', 'age': 22}
print(course)     #Computer Science

#--------------------------------------------------------------------------------------------------
#Use Case of Dictionaries 
'''
Fast Lookups: Dictionaries provide quick access to values based on their keys, making them much faster than lists for lookups.

Data Organization: They are perfect for organizing complex data where you need to associate pairs of related information.

Configuration Files: Dictionaries are often used to store settings or configurations, where each key represents a setting, and each value represents its option.

'''
#----------------------------------------------------------------------------------------------------

