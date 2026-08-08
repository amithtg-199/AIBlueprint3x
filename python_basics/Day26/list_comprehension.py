# num_list = [1, 2, 3, 4]
# '''Here we used list comprehension where we used what operation we need to do on list to get a new list'''
# new_num_list = [n +1 for n in num_list]
# print(new_num_list)

# '''List of Char using List comprehension'''
# name = "Amith"
# char_name = [letter for letter in name]
# print(char_name)

# '''Doubling a number from a range function using List Comprehension'''
# double_num = [ num+num for num in range(1,6)]
# print(double_num)

# '''Conditional List comprehension'''
# names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie", "Dave"]
# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

# '''Coding challenge'''
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [num for num in numbers if num%2 == 0]
# print(result)

'''Challanege'''
from itertools import zip_longest
with open(r"Day26\file1.txt") as f:
    file1 = [num.strip() for num in f.readlines()]
with open(r"Day26\file2.txt") as f:
    file2 = [num.strip() for num in f.readlines()]

result = [int(num) for num in file1 if num in file2]

print(result)