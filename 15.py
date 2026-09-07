'''
Random Name Selector

Use the random module to pick a winner from a list of names.
'''

print("\nRANDOM NAME SELECTOR\n")
import random
contestant = []
for i in range (0, 5):
    
    name = input("NAME OF THE CONTESTANT :     ")
    contestant.append(name)
    
print(f"\nThe winner is {random.choices(contestant)}\n")
    
    
    
    
