'''
Given marks of students: marks = [35, 50, 66, 20, 88, 75]
Use map() to add 10 bonus marks to each student.
Use filter() to keep only students who now have 50 or more.
Use reduce() to calculate the total marks of passed students.
Print the updated marks, passed marks, and total marks.

'''
from functools import reduce
marks = [35,50,66,20,88,75]

bonus = list(map(lambda x:x+10, marks ))

passed = list(filter(lambda x : x>=50 ,bonus ))

total = reduce(lambda x, y : x+y ,passed)

top = reduce(lambda x , y : x if x>y else y , passed )

print(f"UPDATED : {bonus}")
print(f"PASSED : {passed}")
print(f"HIGHEST : {top}")
print(f"TOTAL PASSED : {total}")














