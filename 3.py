print()
print("="*100)
print(f"{"-*"*16 }SIMPLE  COLLEGE ADMISSION SIMULATOR {"-*"*16 } ")
print("="*100)
def menu():
    print("KINDLY CHOOSE OPTION FOR SERVICE ")
    print("="*32)

    print("1.ADD STUDENT DETAILS \n2.DISPLAY STUDENT DETAILS \n3.EXIT \n ")
students = []

while True:
    print()
    menu()
    choice =  int(input("Enter the choice [1,2,3] :     ")) 
    if choice==1:
        name = input("Enter student name :  ")
        age = int(input("Enter Student age :   "))
        location= input("Enter Student Location :   ")
        store = (f"NAME = {name},    AGE = {age},     LOCATION = {location}.")
        students.append(store)
        print()
        print("STUDENTS DETAILS ARE ADDED .")   
    elif choice==2:
        print("DETAILS :-")
        print()
        print(students)
        print()
    elif choice==3:
        print()
        print("THANK YOU FOR VISITING OUR SITE 🙏\nCOME AGAIN")
        break      
    else:
        print()
        print("YOU CHOOSE WRONG OPTION TRY AGAIN ")
        