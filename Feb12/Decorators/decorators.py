def decor(func):
    def inner(name):
            if name == 'Ayush':
                print(name,'is Teaching Java')
            else:
                func(name)
    return inner

@decor
def choice(name):
        print(name,"Is Teaching Python")

choice('Ayush')
choice('Akash')            

'''
Output 

Ayush is Teaching Java
Akash Is Teaching Python

'''