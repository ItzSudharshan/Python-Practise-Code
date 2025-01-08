#Scripting way of Writing the code 
print ('Hello World')

#procedural way of Writing the code 
def message() :
    print("hello World")
    
message()


#Object Oriented way of writing the code 
class Demo:
    def instance_method(self):
        print("Inside Instance Method, Hello World is being Printed")
        
        
d1 = Demo()
d1.instance_method()

'''
The Magic Behind Python Code Execution

Definitions

Source Code: The human-readable code you write in Python (.py files).

Python Interpreter: A program that reads and executes Python code line-by-line.

Bytecode: Intermediate, optimized code generated from source code for efficient execution.

Python Virtual Machine (PVM): Executes bytecode and translates it into machine code.

Machine Code: Binary code that the CPU can directly understand and execute.

Examples
Source Code Example:
print("Hello, world!")
Real-World Analogy: Writing a recipe (source code) that a chef (interpreter) follows step-by-step to cook a meal (output).
Key Points

Write Python code in .py files.

The interpreter reads and executes the code line by line.

Source code is compiled into bytecode (.pyc files).

The PVM executes bytecode and translates it to machine code.

Machine code is processed by the CPU, resulting in the final output.


In Python, \n is used to create a new line, while \t is used to add a tab space. 


'''