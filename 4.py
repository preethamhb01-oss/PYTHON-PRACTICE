class Account:
    def __init__(self, id, u_name, balance = 0):
        self.id = id
        self.u_name=u_name
        self._balance =balance
    def cheak_balance(self):
        print(f"\nCURRENT BALANCE IS :    {self._balance}")
    
    def deposit(self, amount):
        self._balance +=amount
        print(f"DEPOSITED AMOUNT : {amount}\nUPDATED BALANCE : {self._balance}")
        
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -=amount 
            print(f"\n WITHDRAW :   {amount}\nUPDATED BALANCE : {self._balance}")
        else:
            print("INSUFFICIENT BALANCE")
            
class CurrentAccount(Account):
    def __init__(self, id, u_name, balance=0,overdraft =1000):
        super().__init__(id, u_name, balance)
        self.overdraft = overdraft
        
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft :
            self._balance = self._balance -amount 
            print(f"\n WITHDRAW :   {amount}\nUPDATED BALANCE : {self._balance}")
        else:
            print("OVERDRAFT LIMIT IS CLOSED")
            
class SavingAccount(Account):
    def __init__(self, id, u_name, balance=0, interest = 0.05):
        super().__init__(id, u_name, balance)
        self.intesest = interest
        
    def balance_interest(self):
        print(f"INTEREST FOR CURRENT BALANCE : {self._balance * self.intesest}")

class Bank(Account):
    def __init__(self):
        self.accounts ={}
        
    def create_accounts (self,a_type, id, u_name,initial_balance = 0 ):
        if a_type == "savings":
            account = SavingAccount(id ,u_name, initial_balance )
            
        elif a_type == "current":
            account =CurrentAccount(id, u_name, initial_balance)
            
        else:
            print("INVALID ACCOUNT TYPE")
            return None
        
        self.accounts[id] = account
        
        print(f"{a_type . capitalize()} ACCOUNT IS CREATED FOR MR/MRS : {u_name}")
        return account
        
    def get_account(self, id):
        print(self.accounts.get(id), None)
        
#TRYING OUTPUTS -->

bob1=Bank()
bob2=Bank()
a1=bob1.create_accounts("savings", 24, "Preetham", 100)
a2=bob2.create_accounts("current",30, "Sinchana", 1000  )
a1.deposit(1000)
a2.deposit(1000)
a1.withdraw(1200)
a1.withdraw(100)
        
        
            