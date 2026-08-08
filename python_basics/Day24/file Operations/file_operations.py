# import os

# print("Script Location:", os.path.dirname(os.path.abspath(__file__)))
# print("Working Directory:", os.getcwd())

'''Open and close a file trivial method'''
file = open(r"D:\Python_Udemy_Materials\Python_codes_new\Day24\file Operations\my_file.txt")
contents = file.read()
print(contents)
'''Close a file after its operation is done to save resources'''
file.close() 


'''Realtime method'''
with open(r"D:\Python_Udemy_Materials\Python_codes_new\Day24\file Operations\my_file.txt") as file:
    contents = file.read()
    print(contents)


'''Write to a file all data deleted method'''
with open(r"D:\Python_Udemy_Materials\Python_codes_new\Day24\file Operations\my_file.txt", mode="w") as file:
    file.write("Hello new line")

'''append a new line to a file whithout deleting existing content'''
with open(r"D:\Python_Udemy_Materials\Python_codes_new\Day24\file Operations\my_file.txt", mode="a") as file:
    file.write("\nThis is appended line")

# import os

# print(os.path.exists(r"D:\Python_Udemy_Materials\Python_codes_new\Day24\file Operations\my_file.txt"))

# folder = r"D:\Python_Udemy_Materials\Python_codes_new\Day24\file Operations"

# print(os.path.exists(folder))
# print(os.listdir(folder))