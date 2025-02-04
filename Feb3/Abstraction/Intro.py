from abc import ABC, abstractmethod
class Demo1(ABC):
    @abstractmethod
    def dis1(self):
        print('Inside Disp1')
        
        
'''
If Abstract class doesnt have any method than the object for that abstract class can be created 

if abstract class have only concrete method then object for that abstract class can be created and concreate methods can be invoked

'''

class Demo2(ABC):
   def disp2(self):
       print('Inside Disp2') 
       
d2 = Demo2()
d2.disp2()

class Demo3(ABC):
    def info(self):
        print('Inside Info')
    @abstractmethod
    def disp3(self):
        print('Inside Disp3')
        
class Demo4(Demo3):
    pass
d4 = Demo4()
d4.info()

'''
Abstraction helps hide complexity and only exposes the necessary parts of a system.

Abstract Classes are classes that cannot be instantiated and are used to define a blueprint for other classes.

Interfaces in Python can be created using abstract classes, ensuring that subclasses implement the required methods.
'''

'''
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} dollars")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount} dollars")

# Creating instances
credit_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

credit_payment.process_payment(100)  # Output: Processing credit card payment of 100 dollars
paypal_payment.process_payment(150)  # Output: Processing PayPal payment of 150 dollars'''