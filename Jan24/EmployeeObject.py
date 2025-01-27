class Employee:
    company_name = 'code' #class based Variable 
    def __init__(self, name , age , desig):
        self.name = name
        self.age = age           #instance based variable 
        self.desig = desig
        
    def login(self, time):
        print(f'{self.name} logged in at {time}')       #instance methods 
        
    def logout(self, time):
        print(f'{self.name} logged at {time}')
        
    def work(self, hours):
        print(f'{self.name} worked for {hours}')
        
    def getDetails(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")
        print(f"Employee Designation {self.desig}")
        
        
e1 = Employee("Sudharshan", 25, "Software Engineer")
e1.login("10:30")
e1.logout("8:30")
e1.work("8 Hours")
e1.getDetails()

'''
Output 
Sudharshan logged in at 10:30
Sudharshan logged at 8:30
Sudharshan worked for 8 Hours
Employee Name: Sudharshan
Employee Age: 25
Employee Designation Software Engineer
'''