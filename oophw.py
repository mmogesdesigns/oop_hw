# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
# class Vehicle:
#     def __init__(self, reg_num, type, owner):
#         self.registration_number = reg_num
#         self.type = type
#         self.owner = owner
# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle():
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

vehicle1 = Vehicle("ABC123", "Car", "John")
vehicle2 = Vehicle("XYZ789", "Truck", "Alice")
print("Intial owner of vehicle1:",vehicle1.owner)

vehicle1.update_owner("Mary")

print("Updated owner of vehicle1:", vehicle1.owner)


# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
# class Event:
#     def __init__(self, name, date):
#         self.name = name
#         self.date = date

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        num_of_participants =0

    def add_participant(self):
        self.num_of_participants += 1

    def get_participant_count(self):
        return self.num_of_participants
    
