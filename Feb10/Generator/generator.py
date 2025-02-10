def disp():
    return 10
    print('Instruction')
    return 20
    return 30


'''
print(disp())
print(disp())
print(disp())

Normal Function will always return 10 whenever it encounters return statement . Now we will create a Generator Function 
'''
def generator_function():
    yield 10
    yield 20
    yield 30

gen = generator_function()  # Create the generator object once

print(next(gen))  # Outputs 10
print(next(gen))  # Outputs 20
print(next(gen))  # Outputs 30
# print(next(gen))  #StopIteration

