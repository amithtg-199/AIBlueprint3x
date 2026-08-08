import game_data
import random

# for index in range(0, len(game_data.data)):
#     for keys in  game_data.data[index]:
#         print(keys)
a = []
b = []
data=random.choice(game_data.data)
for i in data:
    a.append(data[i])

is_same = False
while is_same is not True:
    b_data=random.choice(game_data.data)
    for i in b_data:
        b.append(b_data[i])
    if a[0] == b[0]:
        is_same = True

print(*a, sep=', ')

print(*b, sep=", ")

