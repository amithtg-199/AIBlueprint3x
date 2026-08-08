#Types of exception

# '''FileNotFoundError'''
# with open("file.txt") as file:
#     file.read()

# '''KeyError'''
# dict = {"key":"value"}
# print(dict["abcd"])

# '''Index'''
# list = [1,2,3]
# print(list[4])

# '''Type'''
# a = "abcd"
# print(a + 2)

# '''Using try, except,else,finally for error handling'''
# try:
#     file = open(r"Day30\file.txt")
#     '''To simulate Key error'''
#     dictionary = {"key":"value"}
#     print(dictionary["abcd"])

# #Exception handling for file exception
# except FileNotFoundError:
#     file = open(r"Day30\file.txt", mode="w")
#     file.write("abcd")

# #Exception handling for Key exception, here we can also catch the exception and print it so that user will understand the error.
# except KeyError as errormessage:
#     print(f"Key {errormessage} not found")

# #When there is no exception then it will execute this block
# else:
#     content = file.read()
#     print(content)

# #If this is present then it will be executed with or without exception
# finally:
#     file.close()
#     print("File was closed.")


# '''Raise your own exception'''
# height = float(input("Enter Height in meters: "))
# weight = int(input("Enter Weight in Kg: "))

# if height > 3:
#     raise ValueError("Height cannot be more than 3 meters")

# bmi = round((weight / height ** 2), 2)

###Challenge try-catch

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]


# def count_likes(posts):

#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes += post['Likes']
#         except KeyError:
#             pass

#     print(f"Total Likes: {total_likes}")

# count_likes(facebook_posts)
    
### Write data to a JSOn file
import json

email = "abcd@gmail.com"
password = "qazWSX!@#123"

'''Always provide data to json module in dictonary format only.'''
new_data = {
    "website":{
        "email": email,
        "password": password
    }
}

# with open(r"Day30\data.json", mode="w") as data_file:
#     ''' Is Used to load the dictionary data into JSON file as JSON format. '''
#     json.dump(new_data, data_file, indent=4)

# with open(r"Day30\data.json") as data_file:
#     '''Used to read JSON file data here fp = filepath'''
#     content = json.load(fp=data_file)
#     print(content)
#     print(content.get("website", {}).get("email"))

item = "Apple"
qty = "10"

new_data = {
    "grocery":{
        "item": item,
        "quantity": qty
    }
}

with open(r"Day30\data.json", mode="r") as data_file:
    '''First get the data from the existing json file''' #Read File
    data = json.load(fp=data_file)
    
    ''' Use update() of JSON module to update the new_data ''' #Update content
    data.update(new_data)

with open(r"Day30\data.json", mode="w") as data_file:
    ''' Write the updated data into the file ''' #Write updated content into the file again
    json.dump(obj=data, fp=data_file, indent=4)


