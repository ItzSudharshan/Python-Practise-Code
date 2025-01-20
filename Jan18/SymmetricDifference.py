'''
Symmetric Difference Between Two Sets

Imagine you are creating a system that helps users find all elements that are unique to each of two sets of numbers (i.e., elements that are in either set, but not in both). Write a Python program that takes two lists of numbers from the user, converts them into sets, and then finds and prints the symmetric difference between these two sets in ascending order.

Your program should:

Allow the user to enter two lists of numbers, separated by spaces. Store them in variables called numbers_list1 and numbers_list2.

Convert both lists into sets called set1 and set2 to eliminate any duplicate values within each list.

Find the symmetric difference of set1 and set2 and store it in a new set called symmetric_diff_set.

Convert the symmetric difference set into a sorted list and print it.

By practicing this, you will learn how to use sets in Python to perform set operations like finding symmetric differences, which is an essential skill for handling collections of unique data and analyzing differences between datasets.

1)
Sample Input

10 20 30 40
20 25 30 35
Sample Output

Symmetric difference of elements: [10, 25, 35, 40]
'''

li1 = set(map(int, input("Please Enter the Elements in the First List without a Space:").split()))
li2 = set(map(int, input("Please Enter the Eleements in the 2nd List Without a Space").split()))

symmetric_different = sorted(li1.symmetric_difference(li2))

print(f"The Symmetric Difference of the 2 lists is {symmetric_different}")