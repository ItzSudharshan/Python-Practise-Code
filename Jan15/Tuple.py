'''
tuple?
Tuples are ordered, immutable collections of items. Like lists, they can contain 
items of different data types, but their items are enclosed in parentheses (( ))




In tuple we can store homogenous as well as Heterogenous Data.
In Tuples we can Store Duplicates
Tuples are Ordered Collection of Data 
Tuple are Immutable : Once we declare the tuple we cannot modify it 

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