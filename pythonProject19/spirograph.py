from turtle import Turtle, Screen, colormode
import random
my_spiral = Turtle()
my_spiral_color = colormode(255)
def random_color():
    r= random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circle(gap_size):
    for _ in range(int(360/gap_size)):
        my_spiral.color(random_color())
        my_spiral.circle(100)
        my_spiral.speed("fastest")
        my_spiral.setheading(my_spiral.heading() + gap_size)
        #if current_heading >= 0:
         #   my_spiral.penup()
          #  return



draw_circle(5)
my_screen = Screen()
my_screen.exitonclick()