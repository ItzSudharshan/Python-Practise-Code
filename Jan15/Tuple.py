'''
tuple?
Tuples are ordered, immutable collections of items. Like lists, they can contain 
items of different data types, but their items are enclosed in parentheses (( ))

A tuple is a collection of items that is ordered and unchangeable. Unlike lists, which allow you to modify their elements, tuples lock their values in place after creation. This makes tuples ideal when you need data to remain constant and unchangeable.


In tuple we can store homogenous as well as Heterogenous Data.
In Tuples we can Store Duplicates
Tuples are Ordered Collection of Data 
Tuple are Immutable : Once we declare the tuple we cannot modify it 
Example : 
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days_of_week)

Output:
('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')



'''
#Tuples wont allow u to add the element , remove the element or even replace the element . Deleting the Whole Object is Allowed
tup1 = (10,22.55,'Kodnest', True,10)
print(tup1)

#Deletes the Complete tuple 1 object is Possible 
del tup1
#print(tup1)  You will get an Error


#Concatination of 2 Tuples are Possible 
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

#Create a SingleTon Tuple:
tup = (10,)
print(tup, type(tup))


new_tup = (10,20,30,40)
#ele1 = new_tup[0]
#ele2 = new_tup[1]


#The below is Called Unmapping of Tuple 
ele1,ele2,ele3,ele4 = new_tup
print("Value of Element1", ele1)
