'''
Simple Contact Book Using a Dictionary

Imagine you are building a simple contact book that keeps track of people and their phone numbers. Write a Python program that allows the user to add names and their corresponding phone numbers to a dictionary, and then display the contact information.

Your program should:

Prompt the user to enter a name and a phone number, separated by a comma (e.g., "John, 1234567890"), and store them in a dictionary called contacts.

Allow the user to enter multiple contact entries until they type "done".

After entering all contacts, print each contact's name along with their phone number.

By practicing this, you will learn how to use dictionaries in Python to manage key-value pairs, which is an essential skill for managing structured data in real-world applications.

1)
Sample Input

Alice, 5555555555
Bob, 4444444444
done
Sample Output

Alice: 5555555555
Bob: 4444444444
'''

contacts = {}

while True:
    user_input = input().strip()
    if user_input.lower() == "done":
        break 
    name, phone_number = user_input.split(",")
    phone_number = user_input.strip()
    contacts[name] = phone_number
    
for name, contacts in contacts.items():
    print(f"{name} : {contacts}")
    