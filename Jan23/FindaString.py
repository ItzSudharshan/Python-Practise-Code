'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over  to .  is excluded.

Question is @https://www.hackerrank.com/challenges/find-a-string/problem
'''
def count_substring(String, sub_string):
    count = 0
    n = len(String) - len(sub_string) + 1
    for i in range(n):
        if (sub_string == String[i:i + len(sub_string)]):
            count += 1
    return count

String = input("Enter the String:")
sub_string = input("Please Enter the Substring:")
result = count_substring(String, sub_string)
print(f"The Number of Substrings present is {result}")