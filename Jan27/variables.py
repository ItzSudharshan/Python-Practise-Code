class Bank:
    Bank_name = 'SBI'
    
    def __init__(self, name, age, balance):
        self.user_name = name
        self.age = age
        self.user_balance = balance
        
    def get_info(self):
        print(f'''User Name: {self.user_name} and User Balance: {self.user_balance} 
for Bank: {Bank.Bank_name}''')  # Using triple quotes for multi-line string

b1 = Bank('Pooja', 25, 56000)
print(b1.Bank_name)  # Accessing class attribute
print(Bank.Bank_name)  # Accessing class attribute directly
b1.get_info() 
