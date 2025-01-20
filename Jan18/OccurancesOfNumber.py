'''
Occurrences of Each Number

Imagine you are creating a system that helps users count how often each number appears in a list. Write a Python program that takes a list of numbers from the user and determines the number of times each unique value occurs in the list.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and store it in a variable called numbers_list.

Convert the input string into a list of integers.

Create a dictionary to count and store the occurrences of each number in the list.

Print each unique number along with its count.

By practicing this, you will learn how to work with lists and dictionaries in Python, which is essential for efficiently handling and analyzing data in many practical applications.

1)
Sample Input

1 2 2 3 3 3 4 4 4 4
Sample Output

1 occurs 1 time(s)
2 occurs 2 time(s)
3 occurs 3 time(s)
4 occurs 4 time(s)
'''

li = list(map(int, input("Enter the Elements in the list with a Space").split()))
occurances = {}

for number in li:
    if number in occurances:
        occurances[number] += 1
    else:
        occurances[number] = 1

for number, count in occurances.items():
    print(f"The Number {number} occurs {count} times")