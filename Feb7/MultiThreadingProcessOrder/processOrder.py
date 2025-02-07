import time
import threading
def process_request(user):
    print(f"Processing Request for {user}")
    time.sleep(5)
    print(f"Request Completed for {user}")
    
    
t1 = threading.Thread(target=process_request, args=("User 1",))
t2 = threading.Thread(target=process_request, args=("User 2",))
t3 = threading.Thread(target=process_request, args=("User 3",))

t1.start()
t2.start()
t3.start()

'''
output

Processing Request for User 1
Processing Request for User 2
Processing Request for User 3
Request Completed for User 1
Request Completed for User 2
Request Completed for User 3

'''