class Student:
    college_name = 'Kodnest'  # Class attribute

    def get_info(self):
        print('College Name is:', Student.college_name)  # Access class attribute
    
    @classmethod
    def change_name(cls, new_name):
        cls.college_name = new_name  

s1 = Student()
s1.get_info()  # Output: College Name is: Kodnest

Student.change_name('St Joseph Engineering College')  # Changing class attribute

s1.get_info()  # Output: College Name is: St Joseph Engineering College
