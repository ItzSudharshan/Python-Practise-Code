'''def disp():
    a = 10 
    b = 0 
    print(a/b)  #You will face an error called Zero Division Error 
    
    
    disp(10, 5)
    disp(10, 5)
    disp(20, 2)
    
'''

def disp(a, b):
    try:
        print('Task Started!')
        print(a/b)
    except:
        print('Some Error Occured and is being Handled ')
    else:
        print('Task Executed without exception ')
    finally:
        print('Task Ended...')
        
        
disp(10, 0)
disp(10, 5)
disp(20, 2)
    
'''
Output : 

Task Started!
Some Error Occured and is being Handled
Task Ended...
Task Started!
2.0
Task Executed without exception
Task Ended...
Task Started!
10.0
Task Executed without exception
Task Ended...

Point:->

Unexpected problems in a program that disrupt its normal flow, like dividing by zero or accessing an invalid list index

try:->Used to keep the logic in which we may get some error 

except:-> Will be executed when exception occured in try block logic 

else:-> will be executed when try block logic  executed without any error 

Finally:->will always be executed Irrespective of Exception occured or not Finally Block will always be executed. 

'''