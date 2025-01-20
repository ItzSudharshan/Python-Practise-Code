'''
Extract a Sublist Using List Slicing

Imagine you are creating a system that helps users extract specific portions of a list using list slicing. Write a Python program that takes a list of numbers from the user and allows them to extract a sublist based on the start and end indices provided by the user.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and store it in a variable called numbers_list.

Convert the input string into a list of integers.

Prompt the user to enter the start index and the end index for the sublist they want to extract.

Use list slicing to extract the specified sublist and print it.

By practicing this, you will learn how to use list slicing in Python, which is a fundamental skill for efficiently manipulating and extracting parts of a list.

1)
Sample Input

1 2 3 4 5 6 7 8 9
2
5
Sample Output

Extracted sublist: [3, 4, 5]
'''
numbers = list(map(int, input("Please Enter the List input with Space").split()))
start_index = int(input("Please Enter the Starting Index:"))
end_endex = int(input("Please Enter the Ending Index:"))
final_result = numbers[start_index:end_endex]
print(f"The Extracted List is {final_result}")