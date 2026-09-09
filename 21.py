'''
2. Calculator
Take two numbers and an operator (+, -, *, /) and perform the operation using match-case.
'''

while True:
    try :
        a= int(input("first number :    "))
        b = int(input("Second number :  "))
        operator = input("Operator :    ")
    except ValueError :
        print("ERROR MAN : !!!!!!ONLY NUMBERS !!!!!!")
    else :


        match operator :
            case "+":
                print(f"SUM  OF  {a} AND {b} : {a+b}")
                break

                
            case "-":
                print(f"SUBTRACTION  OF  {a} AND {b} : {a-b}")
                break
                
                
                
            case "*":
                print(f"MULTIPLICATION OF {a} AND {b}  = {a*b}")
                break
                
            case "/":
                print(f"DIVISION OF {a} AND {b} : {a/b}")
                
                break
                
            case _ :
                print("wrong operator ")
                
                
    finally:
        print("_"*50)
