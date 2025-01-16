'''
#The Common Iterable Object are 
1) List 
2) Tuple 
3) String 
4) Set 
5) range() 
6) Dict()
'''
#List method 
#String  to list 
li1 = list('Kod')   #['K', 'o', 'd']
print(li1)

#tuple to list 

li2 = list((10,20)) #[10, 20]
print(li2)

#Set to list 
li3 = list({100,200})
print(li3)             #[200, 100]

#Dictionary to List 
li4 = list({
    'name' : 'Sudharshan',
    'age': 22
})
print(li4)  #['name', 'age']

#Range to list 

li5 = list(range(1,11))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li5)

#---------------------------------------------------------------------------------------------------------
#Tuple Method (itearble_object)

#list to tuple 
tup1 = tuple([10,20,30])
print(tup1)  #(10, 20, 30)

#Set to  Tuple 
tup2 = tuple({100,200})
print(tup2) #(200, 100)

#Range to tuple 
tup3 = tuple(range(1,11))
print(tup3) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#String to tuple 

tup4 = tuple('Kodnest') 
print(tup4)  #('K', 'o', 'd', 'n', 'e', 's', 't')

#dictionary to Tuple 
tup5 = tuple({ 
    'Name': 'Sudharshan',
    'Age' : 25
})
print(tup5)  #('Name', 'Age')

#-------------------------------------------------------------------------------------------------------------------
#Set Method 
#Set(iterable_object)
s1 = set([10,20,30,40,50])
print(s1)  #Order isnt fixed but duplicate elements are removed 


#---------------------------------------------------------------------------------------------------------------------
#Dict will also accept iterable Object but it should be Present in the form of Key value pairs 
#dict(iterable_object, key:value)

d1 = dict([
    ['Name', 'Sudharshan'],
    ['Age', 25]
])

print(d1)  #{'Name': 'Sudharshan', 'Age': 25}
