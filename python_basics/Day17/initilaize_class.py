class Car():
    def __init__(self):
        # Initialize attributes to describe a car.
        self.make = "Honda"
        self.model = "Civic"
        self.year = 2020

# class Bike():
#     def __init__(self, colour, type, milage):
#         # Initialize attributes to describe a bike.
#         self.colour = colour
#         self.type = type
#         self.milage = milage
    
# my_bike = Bike("Red", "Mountain", 1000)
# print(my_bike.colour)

##Defaults
class BikeType():
    def __init__(self, colour, type):
        self.colour = colour
        self.type = type
        self.milage = 0

my_bike_type = BikeType("Blue", "Road")
print(my_bike_type.milage)