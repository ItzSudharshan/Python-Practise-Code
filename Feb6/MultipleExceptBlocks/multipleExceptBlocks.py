def disp(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('ZeroDivisionError Occurred and Handled')
    except NameError:
        print('NameError Occurred and Handled')
    except TypeError:
        print('TypeError Occurred and Handled')   
    except Exception as e:  # Catch all other unknown errors
        print(f'Some Other Error Occurred and Handled: {e}') 
        
disp(10, 'Kodnest')  # TypeError
disp(10, 0)          # ZeroDivisionError
disp(x, 5)           # NameError (x is not defined)
disp(10)             # TypeError (missing argument)
