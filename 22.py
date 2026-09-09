'''
3. Traffic signal
Take "red", "yellow", or "green" and print:

Red → Stop
Yellow → Wait
Green → Go

'''
print("_"*50)
print("TRAFFIC SIGNAL ")
print("_"*50)
signal = input("ENTER THE COLOUR :   ") 


match signal.upper() :
    case "RED" :
        print("\nSTOP")
        
    case "YELLOW":
        print("\nWAIT")
        
    case "GREEN":
        print("\nGO!")
    
    case _ :
        
        print("\nWRONG PATTERN\n ")