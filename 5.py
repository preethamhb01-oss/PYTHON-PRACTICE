class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Balance for {self.holder_name}: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: {interest}. New balance: {self.balance}")


class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_type, account_number, holder_name, initial_balance=0):
        if acc_type == "savings":
            account = SavingsAccount(account_number, holder_name, initial_balance)
        elif acc_type == "current":
            account = CurrentAccount(account_number, holder_name, initial_balance)
        else:
            print("Invalid account type!")
            return None

        self.accounts[account_number] = account
        print(f"{acc_type.capitalize()} account created for {holder_name}")
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


# 🔥 Simulation Example
bank = Bank()
acc1 = bank.create_account("savings", 101, "Preetham", 1000)
acc2 = bank.create_account("current", 102, "Bro", 2000)

acc1.deposit(500)
acc1.apply_interest()
acc1.check_balance()

acc2.withdraw(2500)
acc2.withdraw(6000)  # overdraft test
acc2.check_balance()
