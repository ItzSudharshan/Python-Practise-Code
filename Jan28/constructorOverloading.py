class demo1:
    def __init__(self):
        self.x = 10
        
    def __init__(self):
        self.x = 200
        
d1 = demo1()
print(d1.x)   #200 is the output 

'''
When we create multiple Constructors in same class then only the last declared constructor will be invoked at the time of object creation . Hence Python doesnt support constructor overloading
'''