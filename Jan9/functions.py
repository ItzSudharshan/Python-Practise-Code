#Without input and without return statement 

def add():
    a =  10
    b = 20
    print('Addtion is', a + b)


     
     

#With input and without return statement 
def sub(a,b):
    print("subtraction is ", a-b)

#Without input and without return statement
def mul():
    return 10 * 20


#With input and with return Statement 
def div(a,b):
    return a/b


add()
sub(19,5)
print(mul())
print(div(200,10))


'''
Interviewer: What are functions in Python, and how do they simplify coding?

Ideal Answer: Functions in Python are like reusable pieces of code that you write once and can use multiple times. They help in automating repetitive tasks, making the code cleaner, easier to read, and more efficient.
-------------------------------------------------------------------------------------------------------------------------------------------

Interviewer: What are the four different types of functions discussed in the session, and what unique purpose does each serve?

Ideal Answer: The four different types of functions discussed are:

No arguments + No return value: These functions don't require any input and don't return any output. They simply perform a task, like playing a song to hype people up.
No arguments + Return value: These functions don't require any input but return a result. An example is a function that tells you the current weather.
Arguments + No return value: These functions require input to perform a task but don't return any output. An example is a function that personalizes a greeting message based on the name and activity provided.
Arguments + Return value: These functions require input and return a result. An example is a function that calculates the area of a rectangle based on the provided length and width

'''