#Write a Python Program to Print all even index element 

# Write a Python Program to Print all even index elements
li = [10, 20, 30, 40, 50, 60]

for idx, ele in enumerate(li, start=1):
    if idx % 2 == 0:  # Check if the index is even
        print(ele)


'''
The enumerate() function in Python is a built-in function that allows you to iterate over an iterable (like a list, tuple, or string) while keeping track of the index of each element. It returns an enumerate object, which yields pairs of the form (index, element) during iteration.

'''
#Another Example
li = [10,20,30]

for idx, ele in enumerate(li):
    print(f"Index of {ele} is {idx}")