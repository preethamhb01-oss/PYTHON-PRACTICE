'''Simple menu
Display:

1. Pizza
2. Burger
3. Pasta
4. Sandwich

Take the user's choice and print the selected item.
'''
print("\nSIMPLE MENU")
print("\nMENU !\n")

while True:
    print("1. Pizza\n2. Burger \n3. Pasta \n4. Sandwich\n5. EXIT")
    try:
        
        order = int(input("\nENTER YOUR NUMBER  TO ORDER  (ONE ITEM PER ORDER) :   "))
    except ValueError:
            print("\nERROR : ONLY NUMBERS ")
    else:
            
            match order :
                case 1:
                    print("\nORDER PLACED : PIZZA\n ")
                    break
                case 2 :
                    print("\nORDER PLACED : BURGER \n")
                    
                    break
                case 3:
                    print("\nORDER PLACED : PASTA\n")
                
                    break
                case 4 :
                    print("\nORDER PLACED : SANDWICH\n ")
                    
                    break
                case 5:
                    print("\nTHANK YOU FOR VISITING\n  ")
                    exit()
                
                    break
                case _:
                    print("\nINVALID NUMBER ")
                    
                
            

