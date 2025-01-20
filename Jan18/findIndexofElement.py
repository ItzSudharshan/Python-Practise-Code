'''
Find the Index of an Element in a Tuple

Imagine you are creating a system that helps users find the index of a specific element in a tuple. Write a Python program that takes a tuple of numbers from the user and allows the user to enter a number to find its index in the tuple.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and convert it into a tuple called numbers_tuple.

Convert the input string into a list of integers and then into a tuple.

Prompt the user to enter a number they want to find in the tuple.

Find and print the index of the given number in the tuple.

If the number does not exist in the tuple, print an appropriate message.

By practicing this, you will learn how to work with tuples in Python and how to find the position of an element in a collection.

1)
Sample Input

10 20 30 40
25
Sample Output

25 is not in the tuple.
2)
Sample Input

1 2 3 4 5
3
Sample Output

The index of 3 in the tuple is: 2
'''

tup = tuple(map(int, input("Please enter the Elements without a Space").split()))
search_number = int(input("Please Enter the Search Number:"))

if search_number in tup:
    print(f"The index of {search_number} is {tup.index(search_number)}")
else:
    print(f"The Number {search_number} isnt present in the Input ")
