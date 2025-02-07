import time
import threading
print(threading.current_thread())
li1 = [1,2,3,4,5]
li2 = ['a', 'b', 'c', 'd', 'e']

def displayDigits(li1):
        for i in li1:
            print(i)
            time.sleep(1)
            

def displayLetters(li2):
        for i in li2:
            print(i)
            time.sleep(1)
            
displayDigits(li1)
displayLetters(li2)

'''
Output 

1
2
3
4
5
a
b
c
d
e

Interviewer: What is multithreading in programming, and how does it compare to single-threaded execution?

Ideal Answer: Multithreading in programming allows multiple parts of a program to run simultaneously, much like handling multiple tasks at once during a dinner party. In a single-threaded execution, tasks are performed one after another, leading to slower performance. Multithreading, on the other hand, enables concurrent task execution, making the program faster and more efficient, especially for tasks that involve waiting, such as reading files or making web request
'''