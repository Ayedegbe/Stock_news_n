# import colorgram
import turtle
import random
"""rgb_colors = []

colors = colorgram.extract('image.jpg',30)
for color in colors: 
    r=  color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)"""
turtle.colormode(255)
my_spots = turtle.Turtle()
is_true = True
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
my_spots.penup()
my_spots.hideturtle()
my_spots.setposition(-300, -260)
for dot_count in range(1, 201):
    my_spots.dot(20, random.choice(color_list))
    my_spots.forward(40)
    if dot_count % 10 == 0:
        if my_spots.xcor() <= -300:
            my_spots.rt(90)
            my_spots.forward(40)
            my_spots.rt(90)
        else:
            my_spots.left(90)
            my_spots.forward(40)
            my_spots.left(90)
print(my_spots.pos())
my_spots.setposition()















my_screen = turtle.Screen()
my_screen.exitonclick()
