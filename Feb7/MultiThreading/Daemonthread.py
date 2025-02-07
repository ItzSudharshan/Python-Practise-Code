import threading
import time

def background_task():
    while True:
        time.sleep(1)
        print("Background task running...")


# Create a daemon thread
thread = threading.Thread(target=background_task, name='daemon Thread')
thread.daemon = True  # Set the thread as a daemon
thread.start()

# Main program ends here

time.sleep(3)
print("Main Thread is dead.")


'''

daemon: A daemon thread runs in the background and automatically exits when the main program ends. This is useful for tasks that should run continuously but don't need to stop the entire program from finishing. A common use case for daemon threads is logging or monitoring tasks that run in the background.

Output 
Background task running...
Background task running...
Main Thread is dead.

'''