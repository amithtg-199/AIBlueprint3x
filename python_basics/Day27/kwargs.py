'''kwargs i.e. keyword args are always used with double astrix **'''
# def calculator(**kwargs):
'''kwargs will also convert the arguments into a dictonary'''
#     print(type(kwargs))
#     print(kwargs)



# def calculator(**kwargs):
'''We can get hold of values of kwargs dictonary as below'''
#     print(kwargs["add"])
#     print(kwargs["multiply"])


# def calculator(n, **kwargs):
#     n += kwargs["add"] #2+4=6
#     n *= kwargs["multiply"] #6*5=30
#     print(n)

# def calculator(n, **kwargs):
#     n += kwargs["add"] #2+4=6
#     n *= kwargs["multiply"] #6*5=30
#     print(n)

# calculator(2, add=4, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.brand = kwargs.get("brand","Nissan")
        self.model = kwargs.get("model","GT-R")

my_car = Car(brand="Nissan")

print(my_car.brand)
print(my_car.model)