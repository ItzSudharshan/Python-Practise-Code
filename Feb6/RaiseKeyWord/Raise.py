def checkAge(age):
    if age < 18:
        raise ValueError('Age must be Greater than 18')

try:
    checkAge(12)  # Now inside the try block
except ValueError as e:
    print('Error Message:', e)
    
'''
Output 

The raise keyword in Python is used to intentionally create an error. This is useful when we want to enforce a rule or handle a situation that Python's normal errors don’t cover.

Error Message: Age must be Greater than 18

'''