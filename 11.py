'''
Append Marks
Ask for student name and marks.
Append the info to marks.txt in this format: Ravi - 85, Ram - 95, Ajay = 99
'''
names=[]
marks=[]
print("Day 33")
for i in range (3):
    name = input(f"{i+1}. ENTER YOUR NAME :     ")
    mark = int(input(f"{i+1}. ENTER YOUR MARKS :   "))
    
    names.append(name)
    marks.append(mark)    
    
with open("marks.txt", "a") as file :
    file.write("Day 33 \n question 2")
    for i in range (len(names)):
        file.write (f"\n{names[i]} = {marks[i]}")