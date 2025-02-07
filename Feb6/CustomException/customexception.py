class PinError(Exception):
    pass

correctPin = 1212
pin = int(input('Enter the 4 Digit Pin'))
try:
    if(pin == correctPin):
        print('Account Unblocked')
    else:
        raise PinError("Entered Pin is ", pin)

except PinError as e:
    print('Incorrect Pin: ', e)
    
'''
Output : 

Enter the 4 Digit Pin121
Incorrect Pin:  ('Entered Pin is ', 121)


Creating Custom Exceptions
Python lets us create our own exception classes. This is useful when normal Python errors like ValueError or TypeError do not fully describe the problem. Custom exceptions let us be more specific about what went wrong.
'''
