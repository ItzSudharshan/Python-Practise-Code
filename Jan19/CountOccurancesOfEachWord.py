'''
Count the Occurrences of Each Word in a Sentence

Imagine you are building a simple word counter that keeps track of how many times each word appears in a given sentence. Write a Python program that takes a sentence from the user and uses a dictionary to count the occurrences of each word.

Your program should:

Prompt the user to enter a sentence and store it in a variable called sentence.

Split the sentence into individual words and use a dictionary to count how often each word appears.

Print each word along with its count.

By practicing this, you will learn how to use dictionaries in Python to manage key-value pairs, which is an essential skill for managing structured data in real-world applications.

1)
Sample Input

This is a test. This test is simple.
Sample Output

This: 2
is: 2
a: 1
test: 2
simple: 1
'''

sentence = input("Please Enter the Sentence:")
li = sentence.split()
d = {}

for i in li:
    i = i.strip(".,!?:;")
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for word, count in d.items():
    print(f"{word}: {count}")