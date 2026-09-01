'''
1.SRP Practice: Create a Book class that only stores details. Create another class that prints book details.
2.OCP Practice: Build a billing system that calculates tax based on ProductType. 
Add Food, Electronics, etc., using subclasses.
3.LSP Practice: Write a class Vehicle and subclasses like Bike, Boat. Avoid breaking behavior.
4.DIP Practice: Make a HomeAppliance system where high-level class Remote works with abstract Appliance,
and you can pass TV, AC, etc.
'''
print("\n1.SINGLE RESPONSIBILITY PRINCIPLE")

class Book:
    def __init__(self, book_name, author_name):
        self.book_name = book_name
        self.author_name = author_name
        
class Details(Book):
    def display(self):
        print(f"\nBOOK NAME : {self.book_name}\nAUTHOR NAME : {self.author_name}")     
        
a= Details("WINGS OF FIRE", "APJ ABDUL KALAM")  
a.display() 

print("\n2. OPEN /LOSE PRINCIPLE")

class Taxes:
    def tax(self):
        print("TAX : 0")
class Food(Taxes):
    def tax(self):
        print("\nFOOD TAX :5%")
        
class Electronics(Taxes):
    def tax(self):
        print("ELETRONICS TAX : 10%")
        
chips = Food()
chips.tax()
mobile = Electronics()
mobile.tax()

print("\n3.Liskov Substitution Principle")

class Vehical:
    def drive(self):
        pass
    
class Bike(Vehical):
    def drive(self):
        print("\nBike is Moving")
        
class Boat(Vehical):
    def drive(self):
        print("Boat is moving")
        
bike = Bike()
boat = Boat()
bike.drive()
boat.drive()
    
print("\n4.Dependency Inversion Principle")

class HomeAppliance:
    def works(self):
        pass

class Tv(HomeAppliance):
    def works(self):
        
        print("\nTV is running ")

class Ac(HomeAppliance):
    def works(self):
        print("AC is running\n ")  
        
class Remote:
    def __init__(self, appliance : HomeAppliance):
        self.appliance = appliance
        
    def works(self):
        self.appliance.works()
        
tv =Tv()
ac=Ac()   
a=Remote(tv)
b=Remote(ac)
a.works()
b.works()
        
        
