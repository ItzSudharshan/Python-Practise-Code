'''
There are 3 types of Control Constructs
1.Conditional: if - else , if - elif
2. Looping: for , while
3. Jumping : break , Continue, pass


'''
'''
def checkAge(age):
    if(age > 18):
        print('Age is Greater than 18')
    else:
        print("Age isnt greater than 18")

checkAge(12)
checkAge(20)



'''
'''
#A Program to display 'child' if age below 18 and age if above 18 display adult if age is above 18 and display senior citizen if age is above 65 
def checkAge(age):
    if(age < 18):
        print('Age is Below 18.(Child)')
    elif(age > 18 and  age < 65):
        print('Age is Above 18 and less than 65(Adult)')
    elif(age > 65):
        print('Age is Above 65(Senior Citizen)')
    else:
        print('Invalid age)
        
checkAge(12)
checkAge(20)
checkAge(70)


checkAge(int(input('Enter the Age')))
'''


#Lopping Statements 
#For Loop 
#Syntax
'''
for control_variable in iterable_object
'''
'''
for i in 'Kodnest':
    print(i)
'''
'''
for j in [10,20,30]:
    print(j + 5)    
'''
'''
for num in range(1, 11):
    print(num)
'''


    
'''
for num in range(11, 21 , 2):
    print(num, end=" ")
'''
'''
#Write a Program to Print even Number from 1 to 10 
for num in range(1,11):
    if num % 2 == 0:
        print(num)
'''
'''
#While Loop
i = 0 
while(i < 10):
    print(i + 100)
    i = i + 1
    
'''
'''
#Jumping control Constructs
#Write a program to print numbers from 1 to 10 if number  is 6 thne skip
for i in range(1, 11):
    if(i == 6):
        continue
    print(i)


'''

'''
#Write a program to print numbers from 1 to 10 if number  is 6 thne stop

for i in range(1, 11):
    if(i == 6):
        break
    print(i)



'''
'''
How do control constructs work in Python? 
Answer: Control constructs are fundamental programming elements that allow you to control the 
flow of execution in your code. They help you make decisions, repeat actions, and perform specific 
tasks based on conditions. 

 In Python, the primary control constructs are:
 
 To make our code flexible and smart, we use different types of control constructs:

Conditional Statements (if-else): These are like making decisions based on the conditions around you. If it's raining, take an umbrella; if it’s sunny, go play cricket.

Loops (for, while): These are like routines where you repeat certain actions until you achieve a goal, like practicing guitar chords every day until you get them right.

Special Controls (Break, Continue, Pass): These are for special situations—like when you want to skip a task, stop a routine early, or just leave a note for yourself to come back and finish something later.

-----------------------------------------------------------------------------------------------------------------------------------------------

Simple if Statement Example:

age = 18
if age >= 18:
    print("You are eligible to vote!")
    
-------------------------------------------------------------------------

if-else Statement Example:

is_hungry = False
if is_hungry:
    print("Time to eat something delicious!")
else:
    print("Maybe just a glass of water.")
    
--------------------------------------------------------------------------


if-elif-else Statement Example

grade = 85
if grade >= 90:
    print("Excellent job!")
elif grade >= 75:
    print("Good work, keep it up!")
elif grade >= 50:
    print("You passed, but there's room for improvement.")
else:
    print("You need to study harder.")
    
    
ThereFore  there are 3 types of Conditional Statements in Python 
-------------------------------------------------------------------------------

Looping Statements

Loops: A way to repeat a block of code multiple times without writing the same instructions again and again.

Python has two main types of loops:

for loops: These are used when you know how many times you want to repeat a task.

while loops: These are used when you want to repeat a task as long as a certain condition is true.

--------------------------------------------------------------------------------------
for Loop Example
A for loop is perfect when you know how many times you need to repeat something. Let’s say you want to count from 1 to 5:

for number in range(1, 6):
    print(number)
    
output:
1
2
3
4
5
    
----------------------------------------------------------------------------------------
while Loop Example

savings = 0
while savings < 500:
    savings += 100
    print(f"You have saved: {savings} rupees")
    
Output:
You have saved: 100 rupees
You have saved: 200 rupees
You have saved: 300 rupees
You have saved: 400 rupees
You have saved: 500 rupees

-------------------------------------------------------------------------------------------

JUMP Statements 

Jump statements in Python allow you to control the flow of loops and functions. They help you make decisions within loops, such as ending, skipping, or pausing iterations.

-------------------------------------------------------------------------------------------
1. break Statement
The break statement is used to exit a loop immediately, even if the loop condition hasn’t been fully met.

for number in range(1, 11):
    if number == 5:
        break
    print(number)

Output:
1
2
3
4

--------------------------------------------------------------------------------------------------
2) continue Statement

The continue statement is used to skip the current iteration and move on to the next one

for number in range(1, 6):
    if number == 3:
        continue
    print(number)
    
Output:
1
2
4
5

--------------------------------------------------------------------------------------------------
3) pass Statement

The pass statement is like a placeholder. It doesn’t do anything but allows you to write syntactically correct code when you don’t want to add functionality yet

for number in range(1, 4):
    if number == 2:
        pass  # Placeholder for future code
    else:
        print(number)
        
Output:
1
3

-------------------------------------------------------------------------------------------------------
4) The return statement is used to exit a function and return a value. 

def greet(name):
    if not name:
        return "No name provided"
    return f"Hello, {name}!"

print(greet("Amit"))
print(greet("") )

Output:
Hello, Amit!
No name provided

------------------------------------------------------------------------------------




'''