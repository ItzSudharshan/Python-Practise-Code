'''
Check if Two Sets are Disjoint

Imagine you are creating a system that helps users determine whether two sets of numbers have no elements in common. Write a Python program that takes two lists of numbers from the user, converts them into sets, and then checks if the sets are disjoint (i.e., they have no elements in common).

Your program should:

Allow the user to enter two lists of numbers, separated by spaces. Store them in variables called numbers_list1 and numbers_list2.

Convert both lists into sets called set1 and set2 to eliminate any duplicate values within each list.

Use a set operation to check if set1 and set2 are disjoint and print an appropriate message.

By practicing this, you will learn how to use sets in Python to perform set operations like checking if sets are disjoint, which is an essential skill for analyzing relationships between datasets.

1)
Sample Input

10 20 30
20 25 30 35
Sample Output

The sets are not disjoint.
2)
Sample Input

1 2 3 4 5
6 7 8 9 10
Sample Output

The sets are disjoint.
'''

li1 = list(map(int, input("Please Enter the Elements in Set1").split()))
li2 = list(map(int, input("Please Enter the Elements in Set2").split()))

set1 = set(li1)
set2 = set(li2)

if set1.isdisjoint(set2):
    print("The 2 Sets are Disjoint")
else:
    print("The 2 Sets are Not disjoint")