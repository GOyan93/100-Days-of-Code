import turtle as t
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for index in range(0, 4):
            snake_piece = t.Turtle()
            snake_piece.shape("square")
            snake_piece.color("white")
            snake_piece.penup()
            x_pos = (index * 20) * (-1)
            snake_piece.setx(x_pos)
            self.snake.append(snake_piece)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)


    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
        else:
            pass


    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
        else:
            pass


    def move_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
        else:
            pass


    def move_down(self ):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
        else:
            pass
