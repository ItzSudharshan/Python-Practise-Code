li = [10,20,30,40,50]
print(type(li), li)
iterable_object = iter(li)
print(type(iterable_object ), iterable_object )

print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
print(next(iterable_object))
# print(next(iterable_object))  #StopIteration

'''
Output:

You can create an iterator from them using the iter() function. Then, you can use next() to manually get each item.

<class 'list'> [10, 20, 30, 40, 50]
<class 'list_iterator'> <list_iterator object at 0x0000029BC5317C10>

10
20
30
40
50
'''