'''
Sum of All Elements in a Tuple

Imagine you are creating a system that helps users calculate the sum of all the elements in a tuple. Write a Python program that takes a tuple of numbers from the user and calculates the total sum of the numbers in the tuple.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and convert it into a tuple called numbers_tuple.

Convert the input string into a list of integers and then into a tuple.

Calculate and print the sum of all elements in the tuple.

By practicing this, you will learn how to work with tuples in Python, which is a fundamental skill for handling immutable collections of data.

2)
Sample Input

10 20 30 5 15
Sample Output

The sum of the elements in the tuple is: 80'''

li = list(map(int, input("Please enter the Elements in the List:").split()))

print(f"The Sum of Numbers in the list {sum(li)}")