''' A list in Python is a mutable, ordered collection of items where each item can be of a 
different data type. Lists are commonly used to store and organize data in a sequential manner and 
offer various built-in methods for manipulation and sorting. 

'''

print('------------------------')
print('Creating a List')
my_list = ["Apple","banana","Orange","Cherry"]

print("Asscessing Elements in the List")
print(my_list[0])
print(my_list[-1])
print('------------------------')
print('Adding and Removing Elements from the List')
my_list.append('Grapes')
print(my_list)
print('------------------------')
print('Removing the Elements from the List')
my_list.remove("banana")
print(my_list)
print('------------------------')
print("Slicing a List")
sublist = my_list[1:3]  #last element isnt Included
print(sublist)
print('------------------------')
