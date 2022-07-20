from turtle import Turtle, Screen
import random
colors = ["red", "green", "yellow", "blue", "violet", "purple", "LimeGreen","DeepSkyBlue", "MediumBlue"]
my_turtle = Turtle()
my_turtle.pensize(random.randint(5,12))

for _ in range(200):
    my_turtle.forward(random.randint(-15,50))
    my_turtle.right(random.randint(0,360))
    my_turtle.color(random.choice(colors))
    my_turtle.circle(random.randint(10,100))
    my_turtle.speed("fastest")








