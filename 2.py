items = 0
print("WELCOME TO OUR SHOPPING SITE ")
print("-"*50)
print("Please choose the service from this site 👩👨 ")
print("-"*50)
def menu():
   
    print(f"1. Add Items to Cart \n2. Remove items \n3. View the Total Price 💵 \n4. EXIT 🚪 ")
    
while True:
    print()
    
    
    menu()
    print("-"*50)
    
    choice = int(input("Enter the Type of service we can provide from our side [1,2,3,4] : choice no. "))
    
    if choice==1:
        add= int(input("Enter the Number of Items Are Ordered :  "))
        items += add 
        print()    
        
        print(f"Currently You have been Ordered {items} of Items ")
    elif choice==2:
        
        remove = int(input ("Enter the number of items want to remove from cart  :  "))
        
        if items>=remove:
            items-=remove
            print()    
            
            print(f"{remove} items are removed from list  and {items} are left in your cart !")
        else:
            print()    
            
            print("You can't remove more items which is not concidered")
        
    elif choice==3:
        price = items * 50
        print()    

        print(f"you have take {items} of items then its price is : ₹{price}")
        
    elif choice ==4:
        print()    
        
        print("THANK YOU FOR VISITING OUR SHOPPING SITE COME AGAIN 😊")
        break
            
    else:
        print("You have entered except [1,2,3,4] options so try again 💪")        
            
   