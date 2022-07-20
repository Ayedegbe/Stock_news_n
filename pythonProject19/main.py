from turtle import Turtle, Screen
import random
my_turtle = Turtle()
colors = ["red", "green", "yellow", "blue", "violet", "purple", "LimeGreen","DeepSkyBlue", "MediumBlue"]
my_turtle.setpos(0,120)
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for shape_side_n in  range(3, 11):
    my_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)












screen = Screen()
screen.exitonclick()