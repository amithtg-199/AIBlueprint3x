# class Animal():

#     def __init__(self):
#         self.number_of_eyes = 2

#     def breathe(self):
#         print("Inhale and Exhale")

# class Fish(Animal):

#     def __init__(self):
#         '''Used to initiliaze all the attributes and methods of Animal class in Fish class also.'''
#         super().__init__()
#         ''' Get the breathe method from parent class Animal'''
#         super().breathe()
#         print("Under water only.")

#     def swim(self):
#         print("Moving in water")

# nemo = Fish()
# nemo.breathe()
# # nemo.swim()

'''Slicing example'''

list = ["a", "b", "c", "d", "e", "f"]

print(list[2:5]) # Get specific items

print(list[2:]) #Get everything from 2 till end of list

print(list[:5]) # get everything from 0 till 5