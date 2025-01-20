'''
Maximum and Minimum Values in a List

Imagine you are creating a system that helps users find the maximum and minimum values in a list of numbers. Write a Python program that takes a list of numbers from the user and determines the largest and smallest numbers in the list.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and store it in a variable called numbers_list.

Convert the input string into a list of integers.

Find and print the maximum and minimum values in the list.

By practicing this, you will learn how to work with lists in Python and use basic functions to find specific values from collections, which is an essential skill in many real-world applications.

2)
Sample Input

10 20 5 40
Sample Output

The maximum value is: 40
The minimum value is: 5'''

li = list(map(int, input("Please Enter the List with a Space").split()))

largest_number = list(set(li))
largest_number.sort(reverse=True)


smallest_number = list(set(li))
smallest_number.sort()

print(f"The Largest Element in the Given List is {largest_number[0]}")
print(f"The Smallest Element in the Given List is {smallest_number[0]}")
