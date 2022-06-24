"""
Program: Vehicle.py
Author: Matt Kimmel
Last date modified: 6/24/2022

The purpose of this program is to create an instance of the class 
Vehicle with an attribute for a vehicle's type as well as the subclass 
Automobile with attributes for year, make, model, doors, and roof. 
Additionally, this program will prompt the user for input to store 
these attributes and output them to display to the user. 
"""

class Vehicle:
    def __init__(self, type):
        self.type = type
        

    def show_car(self):
        """Displays the created instance with it's attributes"""
        print(f"Vehicle type: {self.type}\n")

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)     #Allows Automobile to pass attributes to Vehicle
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
    def show_record(self):
        """Displays the created instance with it's attributes"""
        print(f"Vehicle type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}\n")
    

# Function that interacts with the user to store and access attributes   
def user_prompt():
    answer = input('\nType "add" to add a vehicle or "quit" to exit: ')
    while answer != "quit":
        if answer == "add":
            type = input("Enter the vehicle type (car, truck, etc.): ")
            year = input("Enter the vehicle year: ")
            make = input("Enter the vehicle make: ")
            model = input("Enter the vehicle model: ")
            doors = input("Enter the number of doors (2 or 4): ")
            roof = input("Enter the type of roof (sold or sun roof): ")
            vehicle = Automobile(type, year, make, model, doors, roof)
            print()
            vehicle.show_record()
            answer = input('Type "add" to add another vehicle or "quit" to exit: ')
        else:
            answer = input('Entry not recognized. Type "add" to add a record or "quit" to exit: ')


user_prompt()
    