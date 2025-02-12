def my_decorator(func):
    def wrapper_class():
        print('Something is About to happen!')
        func()
        print('Something has happened already!')
    return wrapper_class

@my_decorator
def say_hello():
    print("hello!")
    
say_hello()


'''
OUTPUT :

Something is About to happen!
hello!
Something has happened already!


'''