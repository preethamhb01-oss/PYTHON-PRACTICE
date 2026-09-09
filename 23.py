'''
Month
Take a month number (1–12) and print the month name.
'''
while True:
    try:
        month = int(input("enter the number :   "))
        
    except ValueError:
        print("ERROR : ONLY NUMBERS")
        

    else:
        match month:
            case 1 :
                print("\nJANUARY")
                break
                
            case 2 :
                print("\nFABRUARY")
                break
            case 3 :
                print("\nMARCH")
                break
            case 4 :
                print("\nAPRIL")
                            
                break
            case 5 :
                print("\nMAY")
                break
            case 6 :
                print("\nJUNE")
                break
            case 7 :
                print("\nJULY")
                break
            case 8 :
                print("\nAUGUST")
                break
            case 9 :
                print("\nSEPTEMBER")
                break
            case 10 :
                print("\nOCTOBER")
                break
            case 11:
                print("\nNOVEMBER")
                break
            case 12:
                print("\nDECEMBER")
                break
            case _:
                print("\nINVALID NUMBER\n")
                
    finally :
        print()
        print("*-"*50)
        print()
        