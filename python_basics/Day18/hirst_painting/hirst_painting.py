
import turtle as t
import random as r

##### used to dervie color pallate of an image- run only once ####
# import colorgram
# rgb_colours=[]
# colour_pallets = colorgram.extract(r'D:\Python_Udemy_Materials\Python_codes_new\Day18\hirst_painting\hirst-1.jpeg', 50)


# for color in colour_pallets:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colours.append((r,g,b))

colour_list = [(199, 159, 114), (69, 91, 129), (148, 85, 52), (218, 210, 115), (136, 160, 193), (27, 32, 47), (179, 161, 35), (58, 33, 22), (184, 145, 164), (123, 70, 93), (137, 175, 153), (76, 115, 78), (143, 25, 15), (61, 30, 41), (187, 97, 82), (120, 28, 43), (46, 59, 94), (99, 118, 172), (178, 96, 114), (33, 51, 44), (99, 159, 85), (66, 84, 23), (215, 174, 192), (217, 181, 172), (218, 206, 7), (159, 210, 191), (178, 186, 214), (46, 72, 59), (41, 74, 79), (168, 201, 209), (105, 135, 144)]
t.colormode(255)
pattern = t.Turtle()
pattern.hideturtle()
current_y = -250
pattern.speed("fastest")
for y in range(10):
    pattern.penup()
    pattern.goto(-250, current_y)
    current_y += 50
    for _ in range(10):
        pattern.dot(20, r.choice(colour_list))
        pattern.penup()
        pattern.forward(45)



screen = t.Screen()
screen.exitonclick()