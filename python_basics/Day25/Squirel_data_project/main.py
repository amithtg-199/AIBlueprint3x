import pandas as pd

df = pd.read_csv(r"Day25\Squirel_data_project\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

'''My method'''
# fur_colours = df["Primary Fur Color"].to_list()
# unique_fur_colors = df["Primary Fur Color"].unique()

# Gray_count = 0
# Cinnamon_count = 0
# Black_count = 0

# for color in fur_colours:
#     if color == "Gray":
#         Gray_count += 1
#     elif color == "Black":
#         Black_count += 1
#     elif color == "Cinnamon":
#         Cinnamon_count += 1

# fur_color_dict = {
#     "fur_color": ["Gray", "Cinamon", "Black"],
#     "Count": [Gray_count, Cinnamon_count, Black_count]
# }

# fur_color_count = pd.DataFrame(fur_color_dict)
# fur_color_count.to_csv(r"Day25\Squirel_data_project\fur_color_count.csv", index=False)

'''Angela Yu Method'''
# gray_squirrels_count = len(df[df["Primary Fur Color"] == "Gray"])
# black_squirrels_count = len(df[df["Primary Fur Color"] == "Black"])
# cinnamon_squirrels_count = len(df[df["Primary Fur Color"] == "Cinnamon"])

# fur_color_dict = {
#     "fur_color": ["Gray", "Cinamon", "Black"],
#     "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
# }

# fur_color_count = pd.DataFrame(fur_color_dict)
# fur_color_count.to_csv(r"Day25\Squirel_data_project\fur_color_count.csv", index=False)

'''Advanced Method using pandas API documentation'''

'''Outputs total count of each color'''
fur_colours = df["Primary Fur Color"].value_counts()

'''Converts to dictionary'''
fur_color_dict = fur_colours.to_dict()
fur_color_dict = {
    "fur_color": ["Gray", "Cinamon", "Black"],
    "Count": [fur_color_dict["Gray"], fur_color_dict["Cinnamon"], fur_color_dict["Black"]]
}

color_df = pd.DataFrame(fur_color_dict)
color_df.to_csv(r"Day25\Squirel_data_project\fur_color_count.csv", index=False)