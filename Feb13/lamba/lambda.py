from functools import reduce

li = [1,2,3,4,5]
def even(ele):
    return ele%2 == 0

#newli = list(filter(even, li))

newli = list(filter(lambda num:num%2 ==0, li))
print(newli)


'''
OUTPUT :


[2, 4]


'''

newli2 = reduce(lambda a, b: a + b, li) 
print(newli2) #Output is 15


square = list(map(lambda num : num ** 2, li))
print(square)  #Output is [1, 4, 9, 16, 25]