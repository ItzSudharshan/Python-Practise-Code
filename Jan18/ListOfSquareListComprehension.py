'''
List of Squares Using List Comprehensions

Imagine you are creating a system that helps users generate a list of squares of numbers using list comprehensions. Write a Python program that takes a list of numbers from the user and creates a new list that contains the squares of those numbers using list comprehension.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and store it in a variable called numbers_list.

Convert the input string into a list of integers.

Use list comprehension to create a new list that contains the squares of the original numbers and print the resulting list.

By practicing this, you will learn how to use list comprehensions in Python, which is a fundamental and efficient way to manipulate lists and transform data.

1)
Sample Input

6 7 8 9 10
Sample Output

List of squares: [36, 49, 64, 81, 100]
'''

li = list(map(int, input("Enter the list elements with a Space").split()))
print("Square of the Given List Elements is ", [i**2 for i in li])