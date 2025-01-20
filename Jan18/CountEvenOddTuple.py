'''
Count Even and Odd Numbers in a Tuple

Imagine you are creating a system that helps users count how many even and odd numbers are present in a tuple. Write a Python program that takes a tuple of numbers from the user and determines the number of even and odd numbers.

Your program should:

Allow the user to enter a list of numbers, separated by spaces, and convert it into a tuple called numbers_tuple.

Convert the input string into a list of integers and then into a tuple.

Calculate and print how many numbers in the tuple are even and how many are odd.

By practicing this, you will learn how to work with tuples in Python and practice using conditional checks to categorize elements in data collections.

1)
Sample Input

10 15 20 25 30
Sample Output

Number of even elements: 3
Number of odd elements: 2'''

li = list(map(int, input("Please Enter the List with a Space ").split()))

even_numbers = 0
odd_numbers = 0
for i in li:
    if i % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print(f"The NUmber of Even Numbers in the List is {even_numbers}")
print(f"The Number of Odd numbers in the list is {odd_numbers}")