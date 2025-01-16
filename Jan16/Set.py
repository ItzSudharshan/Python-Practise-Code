s1 = {10, True, 'Kodnest', 10, 20, 55.44}
print(s1, type(s1))

'''

1) In Set we can store Homogenous as well as Heterogenous Data 
2)  Set is an Unordered Collection of Data  hence Set doesnt support indexing 
3) The order which u entered the data is different from the ordered which you have got hence it is called as Unordered Collection of Data 
4) In Set we cannot store Duplicate Values 

'''
#add() Used to add an Element in the Set 
s1.add(550)
print(s1) #{True, 20, 550, 55.44, 10, 'Kodnest'}


#Remove Use to Remove an Element from the Set 
s1.remove(20)
print(s1) #{True, 550, 55.44, 10, 'Kodnest'}

#Pop without index will delete and return one element 
popped_element = s1.pop()  
print(popped_element)
print(s1)  #{550, 55.44, 10, 'Kodnest'}


#deleting An Entire Set can be Done using del . Deleting specific element using index isnt allowed . Remove can be used specific element 
del s1
#print(s1) Error 


'''
What is a Set?
A set is a collection of items in Python that is unordered. It also does not allow duplicates. 

Example my_set = {1, 2, 3, 4, 5}
print(my_set) 

output {1, 2, 3, 4, 5}

Using the Set function 
numbers = set([1, 2, 3, 4, 4, 5])
print(numbers)

{1, 2, 3, 4, 5}

'''

'''
Common use Cases for the Sets are :->

Removing Duplicates: Sets are great when you need to remove duplicate items from a list.

Membership Testing: Sets are very fast for checking whether an item exists in them, much faster than lists.

Mathematical Operations: Sets allow you to do things like unions, intersections, and differences easily, which is useful in many real-life scenarios, like combining groups or finding similarities.

'''