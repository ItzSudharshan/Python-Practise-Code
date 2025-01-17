#Write a Program which is Able to Count the Occurances of the Number in the List 
input = list(map(int, input('Please Enter the Elements With a Space').split()))

d = {}

for i in input:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
for num,count in d.items():
    print(f"{num} occurs {count} times")
    
    
'''
Output 
Please Enter the Elements With a Space 10 10 20 30 40 50
10 occurs 2 times
20 occurs 1 times
30 occurs 1 times
40 occurs 1 times
50 occurs 1 times

'''