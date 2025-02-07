import time
import threading

print(threading.current_thread())  # This will display the main thread

li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']

def displayDigits(li1):
    print(t1.is_alive())
    for i in li1:
  
        print(f"{threading.current_thread().name}: {i}")
        time.sleep(1)
   

def displayLetters(li2):
    print(t2.is_alive())
    for i in li2:

        print(f"{threading.current_thread().name}: {i}")
        time.sleep(1)


t1 = threading.Thread(target=displayDigits, args=(li1,), name="tester")
t2 = threading.Thread(target=displayLetters, args=(li2,), name="developer")




t1.start()
t1.join()
t2.start()
t2.join()
'''
Key Methods for Multithreading
start(): This method starts a thread, which means it begins running the function you assigned to it. When you call start(), the thread begins running in the background along with other threads.

Analogy: Imagine you have a group project, and each team member has a task to complete. When you tell one member to start working, they begin their task while everyone else also works on theirs. Calling start() is like giving the go-ahead for someone to begin their task.

Example:

import threading

def print_hello():
    print("Hello from thread!")

# Create a thread
thread = threading.Thread(target=print_hello)
thread.start()  # Start the thread
Explanation: In this code, we create a new thread to run the print_hello() function. When we call start(), the thread runs and prints "Hello from thread!" while the main program keeps going.

join(): This method waits for a thread to finish before continuing with the rest of the program. When you call join(), the main program pauses until the specified thread is done running.

Analogy: Imagine you're baking a cake, and you need to let the cake cool before you can add icing. You have to wait until it's ready. The join() method is like waiting for the cake to cool—everything else is paused until that task is done.

Example:

import threading

def print_numbers():
    for i in range(1, 4):
        print(f"Number: {i}")

# Create a thread
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Wait until thread completes

print("Thread has completed, continuing the program.")
Explanation: Here, we create a thread to run the print_numbers() function. After starting the thread, we call join(), which pauses the main program until the thread has finished printing all the numbers. Only then does the program continue.

is_alive(): This method checks if a thread is still running. It returns True if the thread is still running and False if it has finished. This is useful if you want to see whether a thread is still doing its job.

Analogy: Imagine you ask your friend to make dinner, and you keep peeking into the kitchen to see if they are still cooking. If they are, you keep waiting; if they aren't, you know the food is ready. is_alive() is like peeking in to check if the thread is still active.

Example:

import threading
import time

def print_message():
    time.sleep(2)
    print("Message from thread!")

# Create and start a thread
thread = threading.Thread(target=print_message)
thread.start()

# Check if the thread is alive
print(f"Is thread alive? {thread.is_alive()}")
Explanation: In this example, the thread runs the print_message() function, which takes a 2-second pause before printing. We use is_alive() to check if the thread is still running, which helps us understand whether the thread has finished or not.

name: You can give each thread a name to help keep track of what each one is doing. This is helpful when you have multiple threads running at the same time.

Analogy: Imagine giving everyone in your group a title, like "Designer" or "Developer," so you can easily refer to them. Giving a thread a name helps you keep track of what each thread is doing, just like giving a title to a group member.

Example:

import threading

def print_hello():
    print(f"Hello from {threading.current_thread().name}!")

# Create a thread with a name
thread = threading.Thread(target=print_hello, name="MyThread")
thread.start()
Explanation: In this example, we create a thread and give it the name "MyThread." When the thread starts, it prints a message that includes its name, which helps us know exactly which thread is running.


'''