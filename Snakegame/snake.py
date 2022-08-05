from turtle import Turtle
STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 10


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        for point in STARTING_POINT:
            self.add_body(point)

    def add_body(self,point):
            snake = Turtle("square")
            snake.penup()
            snake.color("brown")
            snake.goto(point)
            self.snake_body.append(snake)

    def extend(self):
        self.add_body(self.snake_body[-1].position())


    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(MOVE)



    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading != 90:
            self.head.setheading(270)


    def left(self):
        if self.head.heading != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading != 180:
            self.head.setheading(0)



