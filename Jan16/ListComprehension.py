#List Comprehension 
#[expression for i in iterable_object condition]
li1 = [1,2,3,4,5]
'''   
sq_li = []

for i in li1:
    sq_li.append(i**3)  #Double Astrik Power
    
    
print(li1)     #[1, 2, 3, 4, 5]
print(sq_li)   #[1, 8, 27, 64, 125]

''' 

#When we have only if part then write it after for loop
#Duplicate List
duplicate_li1 = [i for i in li1]  #[1, 2, 3, 4, 5]

#Get Input Numbers from List 
even = [i for i in li1 if i % 2 == 0]  #[2, 4] 

#Get Square of the Elements from the list 
square_list = [i**2 for i in li1]  #1, 4, 9, 16, 25]

#Adding +2 to each Element 
new_li1 = [ele+2 for ele in li1]  #[3, 4, 5, 6, 7]

print(duplicate_li1)
print(even)
print(square_list)
print(new_li1)

#When we have if else both then write it before for loop 
#if and Else in List Comprehension 
even_list = ['even' if i%2== 0 else 'Odd' for i in li1]
print(even_list)  #['Odd', 'even', 'Odd', 'even', 'Odd']


#Nested for Loops for List Comprehension 
li = [[10,20], [30,40], [50,60]]
new_li1 = [ele for i in li for ele in i]
print(new_li1)   #10, 20, 30, 40, 50, 60]


'''
List comprehension is a simple way to create lists. Instead of writing multiple lines of code with loops to add items to a list, list comprehensions let you do it all in one line. This makes your code easier to read and reduces the chances of making mistakes. It’s a shortcut that saves time and makes your code look cleaner.

Example :
Syntax:
[expression for item in iterable]


Without List Comprehension:
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(doubled)

Output : -> [2, 4, 6, 8, 10]


With List Comprehension:
doubled = [num * 2 for num in numbers]
print(doubled)
[2, 4, 6, 8, 10]


Example: Filtering Even Numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

Output : -> [2, 4]



'''