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

'''
Difference Between List and Tupple

----------------------LIST--------------------
1) List is Represented by []
2) List is Mutable . Once List is Created we can do some changes in it 
3) If the content is not fixed and keeps on changing we need to make use of list 
4) List Objects cannot be used as keys for dictionaries because it requires values to be immutable and hashable


----------------TUPLE-----------------------------
1) Tuple is Represented by ()
2) Tuple is Immutable . Once a tuple is created we cannot do chnages to it 
4) if content is fixed and doesnt chnage tuple is to be used 
5) Tuple objects can be used as keys for dictionaries because its values are immutable and hashable

'''