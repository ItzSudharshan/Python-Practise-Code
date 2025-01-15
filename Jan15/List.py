
'''

List ??

Lists are ordered, mutable collections of items. They can contain items of different 
data types, and their items are enclosed in square brackets ([ ]).
--------------------------------------------------------------------------------------------------------------------
 A list in Python is a mutable, ordered collection of items where each item can be of a 
different data type. Lists are commonly used to store and organize data in a sequential manner and 
offer various built-in methods for manipulation and sorting. 
-------------------------------------------------------------------------------------------------------------------
Difference Between List and Tuple 

List                                                                Tuple 
1)List is an Ordered Collection of Mutable Elements               1)Tuple is an Ordered Collection of Immutable elements of different
of Different Data Types which is enclosed                          datatypes seperated by commas and enclosed within ()
inside [](Square Bracket)   

2) List Objects are mutable . Once                                 2) Tuple objects are imutable . Once we create a tuple object
we create a list we can perform changes on it.                         changes cannot be done to it.

3) If content is not fixed and keeps changing                      3) If Content is fixed make use of Tuple
you can make use of list 


4) List Object cannot be used as keys for dictionaries            4)Tuple objects can be used as keys for dictionaries because 
because keys should be Hash table and immutable                     keys should be hashable and immutable 
--------------------------------------------------------------------------------------------------------------------------
'''
'Featurs of List DataType'
'''
In List we can Store Homogenours as well as Heterogenous types of Data 
In List we can also Store Duplicate Values
List is an Ordered Collection of Data . order of Insertion will remain as it is in the Output
List are Mutable . Once we declare the list we can miodify 

'''
#Creating a List To create a list, use square brackets [] with items separated by commas.
li1 = [10,20,30,40,45,True,'Kodnest']
print(li1, type(li1))
#----------------------------------------------------------------------------------------------------------------------------------
#Accessing Items in a List
#To get an item from a list, you use an index. Python lists start at index 0, which means the first item is at position 0, the second at position 1, and so on.
print(li1[1]) #Answer:-> 20
#-----------------------------------------------------------------------------------------------------------------------------
#Append() method will add an element at the end of the list 
li1.append(300)
print(li1)

#--------------------------------------------------------------------------------------------------------------------
#Adding Items

#Inserting value  #insert(index, element) Inserts an element at specified Index 
li1.insert(1, 15)
print(li1) #[10, 15, 20, 30, 40, 45, True, 'Kodnest', 300]

#--------------------------------------------------------------------------------------------------------------------

#Removing the Elements  remove(ele) -> Remove the first Occurance of the Specified Ele
li1.remove(20)
print(li1) #[10, 15, 30, 40, 45, True, 'Kodnest', 300]
#------------------------------------------------------------------------------------------------------------
#Membership Operators 
#in and #Not in
print(2000 in li1)
print(2000  not in li1)
#----------------------------------------------------------------------------------------------------------------

#pop without argument will delete adn return last element from the lsit 
removed_element = li1.pop()
print(removed_element)   #[10, 15, 30, 40, 45, True, 'Kodnest']
print(li1) 

#------------------------------------------------------------------------------------------------------------
#Pop with argument will delete element at specified index
removed_element = li1.pop(3)
print(removed_element)   #[10, 15, 30, 45, True, 'Kodnest']
print(li1) 

#------------------------------------------------------------------------------------------------------
#Del 
del li1[1]
print(li1)

#----------------------------------------------------------------------------------------------------------
'''

List Slicing in Python

List slicing is a way to get specific parts of a list by using indices. Indices are the positions of items in a list, represented by numbers starting from 0. You use a colon symbol : inside the square brackets to indicate the start and end positions of the slice.

list_name[start:end]

start: The index where the slice begins (this value is included).

end: The index where the slice ends (this value is not included).

Example numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get a slice from index 2 to index 5
slice_1 = numbers[2:6]
print(slice_1)

Output [2, 3, 4, 5]

#----------------------------------------------------------------------------------------------------------------------------
Slicing with Steps

You can also add a step value to your slice to get every nth item. This is like telling Python, “Grab every 2nd or 3rd item,” which is really useful for working with patterns in data.
# Get every 2nd item from the list
slice_4 = numbers[::2]
print(slice_4)
Example: [0, 2, 4, 6, 8]

# Get every 3rd item from the list
slice_5 = numbers[::3]
print(slice_5)
Example : [0, 3, 6, 9]


Negative Indices and Slicing

# Get the last 3 items from the list
slice_6 = numbers[-3:]
print(slice_6)

Example : [7, 8, 9]


#------------------------------------------------------------------------------------------------------------------------

Combining Slicing Techniques

# Get every 2nd item from index 1 to 8
slice_7 = numbers[1:9:2]
print(slice_7)
'''