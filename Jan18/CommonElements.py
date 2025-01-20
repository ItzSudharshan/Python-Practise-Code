'''
Find Common Elements Between Two Sets

Imagine you are creating a system that helps users find the common elements between two sets of numbers. Write a Python program that takes two lists of numbers from the user, converts them into sets, and then finds and prints the common elements in ascending order.

Your program should:

Allow the user to enter two lists of numbers, separated by spaces. Store them in variables called numbers_list1 and numbers_list2.

Convert both lists into sets called set1 and set2 to eliminate any duplicate values within each list.

Find the common elements between set1 and set2 and store them in a new set called common_elements_set.

Convert the set of common elements into a sorted list and print it.

By practicing this, you will learn how to use sets in Python to perform set operations like finding intersections, which is an essential skill for handling collections of unique data and comparing datasets.

1)
Sample Input

1 2 3 4 5
3 4 5 6 7
Sample Output

Common elements: [3, 4, 5]
'''

li1 = list(map(int, input("Please Enter the Elements of List1").split()))
li2 = list(map(int, input("Please Enter the Elements of List2").split()))

common_elements  = list(set(li1) & set(li2))

print(f"The Common Elements  between the 2 sets is {common_elements}")
