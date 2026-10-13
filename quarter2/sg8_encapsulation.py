#code
class BankAccount: # This is the class for the code
    def __init__(self, account_number: int, balance: float): #This is thecause for the attributes in the class. It basically starts the attributes of the class
        self.set_account_number(account_number)
        self.__balance = float(balance)
        print("Account 1")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")
        
    def set_account_number(self, account_number: int): #This is what defines the administrator
        self.__account_number = account_number
    
    def set_balance(self, balance: float): #This is what defines the administrator
        print(f"Updated Balance to {balance}")
        if balance < 0:
            print("Balance must not be a negative number") # This is a signal that the number inputted by the user is negative.
        else:
            self.__balance = float(balance)
            

    
    @property #@poperty is used to define a method as a property
    def account_number(self):
        return self.__account_number
    @property
    def balance(self):
        return self.__balance

a1 = BankAccount(20121, 1618) # These are the values within the account
a1.set_balance(2000)
a1.set_balance(-260)

print("Account 1") # This is the final output for the code
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance}")
    
