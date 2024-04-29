#!/usr/bin/env python3

# Classes
# https://docs.python.org/3/tutorial/classes.html
# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Each class instance can have attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by its class) for modifying its state.

# Define a new class called Garment
# __init__() is called upon instantiation, meaning new instances of the class will execute
# any code within __init__() upon creation. This can also be used to assign properties to a class.
class Garment():
    def __init__(self, name, garment_type, color, capacity):
        self.name = name
        self.type = garment_type
        self.color = color
        self.capacity = capacity


# Create a new instance of the class stored in a variable called 'my_garment'
my_garment = Garment("My favorite shirt", "shirt", "blue", 2)
print(my_garment)

# Properties of an object can be accessed using the dot operator
print(my_garment.name)


# Create another Class, Drawer, to store Garments
class Drawer():
    def __init__(self, max_capacity):
        self.current_capacity = 0
        self.garments = []
        self.max_capacity = max_capacity

    # Within the class, we can create functions
    # Not that like __init__(), we need 'self' as the first argument in Class functions
    def count(self):
        return len(self.garments)

    def can_fit_new_garment(self, garment_capacity):
        if self.current_capacity + garment_capacity > self.max_capacity:
            return False
        return True

    def add_garment(self, garment):
        self.garments.append(garment)
        self.current_capacity += garment.capacity


my_drawer = Drawer(20)
print(my_drawer.garments)

# Use class function to add a garment
# Class functions are also accessed with the dot operator
my_drawer.add_garment(my_garment)
print(my_drawer.garments)
# Print the name of the first item in my_drawer's garments
print(my_drawer.garments[0].name)
print(my_drawer.can_fit_new_garment(2))
print(my_drawer.count())
