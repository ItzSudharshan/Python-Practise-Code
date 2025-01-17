#reverse Method () will reverse the Original object 
li = [10,5,20,7,4]
print("Before Reverse: ", li)
li.reverse()
print('After Reverse : ', li)

#Reversed Method: It will always return iteratable Object 
#Syntax is Reversed(iterable obeject)
li2 = [11,6,8,22]
reversed_list = list(reversed(li2))
print(reversed_list)


li3 = [1,5,2,9]
new_reverse_list = list(reversed(li3))  #creating a new Reversed List 
print(new_reverse_list)  
li3.reverse()  #original List it Reverses 
print(li3)