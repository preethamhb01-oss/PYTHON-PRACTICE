'''
File Reader:

Ask the user for a file name and try to open it.
Show error message if file doesn't exist.
Use finally to print “Program End

'''
while True:
    print("\nFILE READER ")

    try :
        filename = input("\nENTER FILE NAME :  ")
        with open (filename, "r") as file:
            display = file.read()
            print(display)
            break
            
    except FileNotFoundError:
        print("\nERROR : FILE IS NOT IN SYSTEM ")
    finally:
        print("\nPROGRAM ENDED ")
        print("_"*55)

        
    