#First way of accepting input from the list 
'''
li = []
num = int(input('Please Enter the Number of Elements: '))
for i in range(num):
    ele = int(input(f'Enter the Element at Index {i}: '))
    li.append(ele)

print(li)   

'''
'''
Output

Please Enter the Number of Elements: 4
Enter the Element at Index 0: 1
Enter the Element at Index 1: 2
Enter the Element at Index 2: 2
Enter the Element at Index 3: 3
[1, 2, 2, 3]

'''
'''
#Second way of accepting input from the user 
li = input('Enter Space Seperated Elements:')
print(li, type(li))
li = li.split()  #['10', '20']
print(li)

li = list(map(int, li))
print(li)  #[10, 20]
'''
'''
tup = tuple(map(int,input('Enter the Space Entered Elements:').split()))
print(tup)
'''

li = list(map(int, input("Enter space-separated numbers: ").split()))
print("Input list:", li)
print("Even numbers:", [i for i in li if i % 2 == 0])
