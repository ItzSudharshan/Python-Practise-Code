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
        print(a/b)
    except:
        print('Some Error Occured and is being Handled ')
        
        
disp(10, 0)
disp(10, 5)
disp(20, 2)
    
'''
Output : 
Some Error Occured and is being Handled 
2.0
10.0
'''