def division(func):
    def inner(a, b):
        if b == 0:
            print('Error: b should not be 0')  # Proper error message
        else:
            return func(a, b)                 # Return the division result
    return inner  # Return the inner function

@division
def div(a, b):
    print('Division is:', a / b)

# Test Cases
div(10, 2)  # Valid division
div(10, 0)  # Handles division by zero


'''
Output:

Division is: 5.0
Error: b should not be 0

'''