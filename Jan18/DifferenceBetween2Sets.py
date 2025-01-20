'''
Find the Difference Between Two Sets

Imagine you are creating a system that helps users find the difference between two sets of numbers. Write a Python program that takes two lists of numbers from the user, converts them into sets, and then finds the difference between the first set and the second set.

Your program should:

Allow the user to enter two lists of numbers, separated by spaces. Store them in variables called numbers_list1 and numbers_list2.

Convert both lists into sets called set1 and set2 to eliminate any duplicate values within each list.

Find the difference of set1 from set2 (i.e., elements in set1 but not in set2) and print the result.

By practicing this, you will learn how to use sets in Python to perform set operations like finding differences, which is an essential skill for handling collections of unique data and analyzing relationships between datasets.

1)
Sample Input

1 2 3 4 5
3 4 5 6 7
Sample Output

Elements in Set 1 but not in Set 2: {1, 2}
'''
li1 = list(map(int, input("Please Enter the Elements of List1").split()))
li2 = list(map(int, input("Please Enter the Elements of List2").split()))
difference = list(set(li1)  - set(li2))
print(f"The Set1 elements which are not in Set 2 Elements are {difference}")