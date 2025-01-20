'''
Check if One Set is a Subset of Another

Imagine you are creating a system that helps users determine whether all elements of one set are contained within another set. Write a Python program that takes two lists of numbers from the user, converts them into sets, and then checks if the first set is a subset of the second set.

Your program should:

Allow the user to enter two lists of numbers, separated by spaces. Store them in variables called numbers_list1 and numbers_list2.

Convert both lists into sets called set1 and set2 to eliminate any duplicate values within each list.

Check if set1 is a subset of set2 and print an appropriate message.

By practicing this, you will learn how to use sets in Python to perform set operations like checking subsets, which is an essential skill for handling collections of unique data and analyzing relationships between datasets.

1)
Sample Input

1 2 3
1 2 3 4 5
Sample Output

Set 1 is a subset of Set 2.
'''

s1 = set(map(int, input("Please Enter the Elements with space for the first Set").split()))
s2 = set(map(int, input("Please Enter the Elements with space for the Second Set").split()))

if s1.issubset(s2):
    print("The Set1 is a Subset of Set2")
else:
    print("The Set1 is not a Subset of Set2")