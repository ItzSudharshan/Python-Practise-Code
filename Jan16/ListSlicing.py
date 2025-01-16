#Creating a Sublist from the Main List is Called List Slicing 
#list_name[start:end:step]
li1 = [10,20,30,40,50,60]
sub_list = li1[0:4:1]
print(sub_list)  #[10, 20, 30, 40]

#Default start is Start and Default end is last element and default step is 1
sub_list1 = li1[1::]
print(sub_list1)  #[20, 30, 40, 50, 60]


sub_list2 = li1[::2]
print(sub_list2)  #[10, 30, 50] Alternate Elements are Printed 


#printing Reverse Element in the List 
reverse_list = li1[::-1]
print(reverse_list) #[60, 50, 40, 30, 20, 10]

print(li1[-1::])  #[60]


'''
Q: What is List Slicing ?
Is used to create a Sublist from main List
Syntax : list_name [start:end - 1: steps ]

reverse list[::-1]
only the last element [-1::]


'''