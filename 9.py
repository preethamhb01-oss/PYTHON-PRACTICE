'''
Safe Divider:

Ask two numbers from the user and divide them.
Handle ZeroDivisionError and ValueError.
'''

print("SAFE DIVIDER")
while True:
    try :
        first = int(input("\nFirst :  "))
        second = int(input("\nSecond :  "))
        
        divide = first /second 
        
    except ZeroDivisionError:
        print("error : Zero Can't divide any Integer ")
    except ValueError:
        print("ONLY NUMBERS !")
    else:
        
        print(f"Answer of {first}/ {second} = {divide }")
        break
    finally :
        print("_"*55)
        
        
    
    