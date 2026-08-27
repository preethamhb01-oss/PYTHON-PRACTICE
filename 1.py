
print("<><><><> SIMPLE BANK SIMULATOR 🏦 <><><><>")

balance = 0     
def menu():
    print(f"1. Cheak Balance\n2. Deposit Money \n3. Withdraw Amount \n4.Exit ")

while True:
    menu()
    choise = int(input("Enter your choise : "))

    if choise == 1:
        print(f" Your current balance is : ₹{balance} ")
        
    elif choise == 2:
        deposit = int(input("Enter the Amount to Deposit :  "))
        balance+=deposit
        print(f"Your Account Has been Credited of Amount :₹ {deposit} \nand your current balance is ₹ {balance}")
        
    elif choise== 3:
               
        withdraw_amount = int(input("Enter the Amount to Withdraw :  "))
        if balance > withdraw_amount :    
            balance -= withdraw_amount
            
            print(f"Your Account has been withdrawed  of amount ₹{withdraw_amount} and current balance is ₹{balance}")
        
        else:
            print("Insufficient Balance")
         
    elif choise==4:
        print("EXITING .....\n\t COME AGAIN")
        break
    else:
        print("Invalid Choise choosen by User !!!!!")
        

        
    
    
    
    