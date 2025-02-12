def repeat(num):
    def outer(func):
        def inner():
            for i in range(num):
                func()
        return inner
    return outer

@repeat(num=3)
def msg():
    print('Hello')
msg()

'''
Output

Hello
Hello
Hello

'''