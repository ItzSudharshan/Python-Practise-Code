'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

refer Question @ https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
'''

li = []
N = int(input())

for i in range(N):
    command , *values = input().split()
    values = list(map(int,values))
    
    if command == 'insert':
        li.insert(values[0], values[1])
    elif command == 'print':
        print(li)
    elif command == 'remove':
        li.remove(values[0])
    elif command == 'append':
        li.append(values[0])
    elif command == 'sort':
        li.sort()
    elif command == 'pop':
        li.pop()
    elif command == 'reverse':
        li.reverse()
        