#code
class BankAccount: # This is the class for the code, the code will mainly be revolving around this class.
    def __init__(self, account_number: int, balance: float): #This is the constructor of the class and the "def" is to define a function that is within the class.
        self.set_account_number(account_number) # self is used to access the methods and attributes rather than the whole class
        self.__balance = float(balance)
        print("Account 1")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}") # This prints the initial outcome and the values of the account
        
    def set_account_number(self, account_number: int): #This is what defines the administrator, int means that the value must be an integer
        self.__account_number = account_number
    
    def set_balance(self, balance: float): #This is what defines the administrator, float means that the value has a decimal point.
        print(f"Updated Balance to {balance}")
        if balance < 0:
            print("Balance must not be a negative number") # This message will show up if the value given is negative
        else:
            self.__balance = float(balance)
            

    
    @property #@poperty is used to define a method as a property, it is used to have getters and setters.
    def account_number(self):
        return self.__account_number
    @property
    def balance(self):
        return self.__balance

a1 = BankAccount(20121, 1618) # These are the values within the account
a1.set_balance(2000) # These are the updated values in the account
a1.set_balance(-260) # These are the updated values in the account

print("Account 1") 
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance}") 
# This is the final output for the code which shows the changes applied and wether it may be right or wrong ( the error message will popup if it is wrong because of a negative integer)
    
