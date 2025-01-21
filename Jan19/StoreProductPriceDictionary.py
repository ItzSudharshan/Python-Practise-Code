'''
Store Product Prices

Imagine you are building a simple price list that keeps track of different products and their prices. Write a Python program that allows the user to add product names and their corresponding prices to a dictionary, and then display the product information.

Your program should:

Prompt the user to enter a product name and a price, separated by a comma (e.g., "Milk, 2.50"), and store them in a dictionary called product_prices.

Allow the user to enter multiple product entries until they type "done".

After entering all products, print each product's name along with its price.

By practicing this, you will learn how to use dictionaries in Python to manage key-value pairs, which is an essential skill for managing structured data in real-world applications.

1)
Sample Input

Milk, 2.50
Bread, 1.20
Eggs, 3.00
done
Sample Output

Milk: 2.5
Bread: 1.2
Eggs: 3.0
'''

product_price = {}

while True:
    user_input = input().strip()
    if user_input.lower() == "done":
        break 
    product, price = user_input.split(",")
    price = float(price.strip())
    product_price[product] = price
    
for product, price in product_price.items():
    print(f"{product} : {price}")