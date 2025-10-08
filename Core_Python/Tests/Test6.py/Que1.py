from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, wheels, person):
        self.wheels = wheels
        self.person = person

    def calculate_toll(self):
        pass

class Twowheeler(Vehicle):
    def calculate_toll(self):
        toll = 20
        if (self.person > 2):
            toll += (self.person - 2) * 10
        return toll
        
class Threewheeler(Vehicle):
    def calculate_toll(self):
        toll = 30
        if (self.person > 3):
            toll += (self.person - 3) * 20
        return toll
        
class Fourwheeler(Vehicle):
    def calculate_toll(self):
        toll = 40
        if (self.person > 4):
            toll += (self.person - 4) * 40
        return toll
        
class heavyvehicle(Vehicle):
    def calculate_toll(self):
        toll = 60
        if (self.person > 6):
            toll += (self.person - 6) * 60
        return toll
        
while True:
    print("1. Two wheeler")
    print("2. Three wheeler")
    print("3. Four wheeler")
    print("4. Heavy vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice :"))
    if choice == 5:
        print("Thank you for using toll system")
        break

    person = int(input("Enter the number of persons :"))

    if choice == 1:
        Vehicle = Twowheeler(2, person)
    elif choice == 2:
        Vehicle = Threewheeler(3, person)
    elif choice == 3:
        Vehicle = Fourwheeler(4, person)
    elif choice == 4:
        Vehicle = heavyvehicle(6, person)
    else:
        print("Invalid choice")
        continue

    print(f"Total Toll to pay : {Vehicle.calculate_toll()}")


