# '''Dict Comprehension using condition and walrus operator'''
# import random

# names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie", "Dave"]
# student_scores = {student:random.randint(1,100) for student in names}
# # passed_students = {student:score for student in student_scores if (score := student_scores[student]) > 50}
# '''OR'''
# passed_students = {student:score for (student,score) in student_scores.items() if score > 50}
# print(student_scores)
# print(passed_students)

# '''Challenge'''
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# '''Challenge'''
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}

# print(weather_f)

'''Iterrating through pandas DF'''
student_s = {
    "students":["Alex", "Beth", "Caroline", "Eleanor", "Freddie", "Dave"],
    "scores": ["11", "93", "56", "72", "42", "89"]
}

import pandas as pd

student_scores = pd.DataFrame(student_s)
# print(student_scores)

'''Iterrows function will help to intterate through all the rows in DF and print out the rows as a series object'''
for (index, row) in student_scores.iterrows():
    if row.students == "Dave":
        print(row.students)
        print(row.scores)