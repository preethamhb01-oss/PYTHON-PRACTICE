'''
Create a File and Write

Ask user for 5 super heros  names.
Write them into mcu.txt, one per line.
'''

print("DAY 33")

heros = []
for i in range(5):
    name = input(F"ENTER YOUR {i+1}th SUPER HERO :   ")
    heros.append(name)
    
with open ("mcu.txt", "a") as file :
    for hero in heros :
        file.write(f"\n\tMY FAV SUPER HERO IS {hero}")
        file.write("\n\tOUTPUT OF THE CODE")
    
    

    
    