import random
import my_module
values = random.randint(1,10)
print(values)
print(my_module.my_fav_number)
# Generate Floating random number between 0 (included) and 1(not included)
random_float_0_to_1 = random.random()
print(random_float_0_to_1)
# Generate Floating random number between 0 (included) and 10(not included)
random_float_0_to_10 = random.random()*10
print(random_float_0_to_10)

# Or we can use uniform module to generate it, here it will include 0 and 20 also, but in random only 0 is inlcuded but 1 is not included
random_float_0_to_20 = random.uniform(1,20)
print(random_float_0_to_20)