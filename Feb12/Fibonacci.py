
'''
def fibonacci(num):
    a, b = 0, 1  # Starting values for Fibonacci sequence
    for i in range(num):
        print(a)
        a, b = b, a + b  # Update a and b for the next iteration

fibonacci(10)


'''
'''
output for Non generator function 

1
2
3
5
8
13
21
34

'''
def fibonacci_generator(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        a, b = b, a + b

# Create a generator instance
ref = fibonacci_generator(10)

# Get the first Fibonacci number
#print(next(ref)) #0
#print(ref.__next__())  #1 # Equivalent to ref.__next__() 

# Continue fetching the next 5 Fibonacci numbers
for i in range(5):
    print(next(ref))


'''

Output for Fibonacci Generator Function 

0
1
1
2
3

'''

        