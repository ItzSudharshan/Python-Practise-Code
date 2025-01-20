'''
Average of Numbers in a List

Imagine you are creating a system that helps users calculate the average of all numbers in a list. Write a Python program that takes a list of numbers from the user and calculates the average of all elements.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and store it in a variable called numbers_list.

Convert the input string into a list of integers.

Calculate and print the average of all numbers in the list.

By practicing this, you will learn how to work with lists in Python and use basic functions to calculate values from collections, which is an essential skill in many real-world applications.

2)
Sample Input

10 20 30 40
Sample Output

The average of the list is: 25.0
'''


number = list(map(int, input("Please Enter the Number List:").split()))
print(f"The average of the Given List is {sum(number)/len(number)}")