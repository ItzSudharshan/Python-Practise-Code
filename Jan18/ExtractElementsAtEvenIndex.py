'''
Extract Elements at Even Indices Using Tuple Slicing

Imagine you are creating a system that helps users extract elements from a tuple that are located at even indices. Write a Python program that takes a tuple of numbers from the user and extracts the elements that are present at even indices.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and convert it into a tuple called numbers_tuple.

Convert the input string into a list of integers and then into a tuple.

Use tuple slicing to extract the elements at even indices and print them.

By practicing this, you will learn how to use tuple slicing in Python, which is a fundamental skill for efficiently manipulating and extracting parts of an immutable collection of data.

2)
Sample Input

10 20 30 40 50 60
Sample Output

Elements at even indices: (10, 30, 50)
'''

tup = tuple(map(int, input("Please Enter the Elements with a Space:").split()))

Element_at_even_index = tup[0::2]

print(f"The Elements at Even index are {Element_at_even_index}")