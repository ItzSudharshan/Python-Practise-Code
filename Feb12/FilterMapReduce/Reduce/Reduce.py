from functools import reduce

# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Use reduce to apply the function cumulatively to the elements in the list
total_product = reduce(multiply, numbers)

print(total_product)

'''

OUTPUT:
120

'''