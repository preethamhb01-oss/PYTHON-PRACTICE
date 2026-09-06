'''
Read and Count Lines

Read any file and count how many lines it has.
Example: How many students are listed?
'''
with open ("playing11.txt", "r") as file :
    lines = file.readlines()
    print(f"\n NUMBER OF PLAYERS IN LIST  : {len(lines)}\n")