li = [1,2,3,4]


def checkEven(num):
    return num % 2 == 0

even_li = list(filter(checkEven, li))
print(even_li)

'''
Output

[2, 4]

'''