class Student:
    def learn(self):
        print(self.name, 'is learning')

    def play(self):
        print("Inside Play Method")

# Create an instance and set the name separately
s1 = Student()
s1.name = "Sudharshan"  # Manually setting the name attribute

# Call methods
s1.learn()
s1.play()
