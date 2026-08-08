# data = []
# with open(r"Day25\weather_data.csv") as f:
#     for _ in f.readlines():
#         data.append(_.strip())

# print(data)

# import csv

# with open(r"Day25\weather_data.csv") as f:
#     data_files = csv.reader(f)
#     '''Skips first row'''
#     next(data_files)
#     temperature = []
#     for row in data_files:
#         temperature.append(int(row[1]))
# print(temperature)

'''Using Pandas, first we need to install it using "pip install pandas"'''
import pandas as pd

data = pd.read_csv(r"Day25\weather_data.csv")

# '''Converting a data frame into a dictornary using dictinary methods'''
# data_dict = data.to_dict()
# print(data_dict)

# '''Converting a Series into a list'''
# data_list = data["temp"].to_list()

# '''Finding Mean using normal method'''
# average = sum(data_list)/len(data_list)
# print(round(average,2))

# '''Finding Mean using pandas Series.mean function'''
# temp_data = data["temp"]
# average_panadas = temp_data.mean()
# print(round(average_panadas,2))

# max_pandas = temp_data.max()
# print(max_pandas)

# '''To get data in a column'''
# print(data.condition)

# '''Getting a specifc row of data from the DF'''
# print(data[data.day == "Monday"])
# print("=="*10)
# '''To check in the DF series/column a specific string exists (retruns bool, ture or fals)'''
# print(data["day"] == "Monday")

# '''To print a row which has maximum temp'''
# '''Here we are actually fetching the data.temp column (that is a temperature column) and equating each data in that column to max temperature, 
# which ever column matches print that row.'''
# print(data[data.temp == data.temp.max()])

# '''To get Condition on Monday'''
# '''Get the row that matches monday'''
# monday = data[data.day == "Monday"]
# '''Get the condition for monday variable which = Row which contains monday'''
# print(monday.condition)

# '''Convert Mondays temp from celcius to farenhite'''
# monday = data[data.day == "Monday"]
# monday_temp_fh = (int(monday.temp[0]) * 1.8) + 32

# print(f"Temperature for {monday.day[0]} was {monday_temp_fh} in Farenhite and the condition was {monday.condition[0]}")

'''Create a Data Frame from dictionary'''
data_dict = {
    "studenets": ["Amy", "James", "Amith"],
    "scores": [75, 56, 85]
}

student_data = pd.DataFrame(data_dict)

'''Save this DF as a csv file'''
student_data.to_csv(r"Day25\student_data.csv", index=False)
