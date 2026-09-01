print("DAY 31")
while True :
    try:
        print()
        a = input("Enter Your favorite super Hero (No space btw name ) :     ")
        
        if a.upper() !="IRONMAN":
            raise Exception("You choose Wrong Super hero ")
    except Exception as e:
        print(f"Error :{e} ")

    else:
        print(f"Yes  The  great super Hero is {a}")
        break

    finally:
        print("JUST MCU FANS THING ")
        print()