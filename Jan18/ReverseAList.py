'''
Reverse a List Using List Slicing

Imagine you are creating a system that helps users reverse the order of elements in a list using list slicing. Write a Python program that takes a list of numbers from the user and reverses the list using slicing.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and store it in a variable called numbers_list.

Convert the input string into a list of integers.

Use list slicing to reverse the order of elements in the list and print the reversed list.

By practicing this, you will learn how to use list slicing in Python, which is a fundamental skill for efficiently manipulating and extracting parts of a list.

1)
Sample Input

1 2 3 4 5
Sample Output

Reversed list: [5, 4, 3, 2, 1]
'''

#Using List Slicing 
li = list(map(int, input("Please Enter the LIst").split()))
reverse_list = li[::-1]
print(f"The Reversed List using List Slicing Mehthod is {reverse_list}")