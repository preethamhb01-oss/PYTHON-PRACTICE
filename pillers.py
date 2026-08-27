import calendar
y = int(input("Enter the year :  "))

m = int(input("Enter the number of month :  "))
if y <3000 and m <=12:
    
    print(calendar.month(y, m))
    
else:
    print("only limited eddition if want for every year then take premium at ₹ 999")