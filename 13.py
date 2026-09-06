'''
Search From File

Write a program that searches for a name in friends.txt
If found, print "Found!" else "Not Found!"
'''
while True:
    name = input("Enter name to verify:     ")
    with open("friends.txt", "r") as file :
        content = file.read()
        
        if name in content:
            print("Found!")
            break
            
        else:
            print("Not Found !")
        