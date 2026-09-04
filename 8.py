'''
1) Age Verifier:

Ask the user for their age.
If age is valid (number), show in how many years they will be 100 years old.
Handle invalid input gracefully.        
'''
while True:
    print("\nAGE VERIFIER  ")

    try :
        age = int(input("Enter Your Age :- "))
        if age <=0 :
            raise Exception("Write valid Age ")
        if age >100:
            raise Exception("Write valid Age ")
        
    except Exception as e :
        print(f"\nERROR : {e}")
        print("\nretry")
    except ValueError :
        print("\nAGE MUST BE  IN NUMBERS ")
        print("\nretry")
        
    else :
        print(f"\nAge : {age }")
        
        break
        
    finally:
        print("ended")
        

    