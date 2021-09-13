import turtle as t
import time, snake
from food import Food
from scoreboard import Scoreboard


canvas = t.Screen()
canvas.setup(width = 800, height = 600)
canvas.bgcolor("black")
canvas.title("My Snake Game")
canvas.tracer(0)

TOP_BORDER = 290
BOTTOM_BORDER = -290
LEFT_BORDER = -290
RIGHT_BORDER = 290

snake_1 = snake.Snake()
food = Food()
score = Scoreboard()


canvas.listen()
canvas.onkeypress(fun= snake_1.move_left, key= "Left")
canvas.onkeypress(fun= snake_1.move_right, key= "Right")
canvas.onkeypress(fun= snake_1.move_up, key= "Up")
canvas.onkeypress(fun= snake_1.move_down, key= "Down")



def main_game_loop():
    game_is_on = True
    while game_is_on:
        canvas.update()
        time.sleep(0.06)
        snake_1.move()

        # Detect collision with tail
        tail = snake_1.get_tail_pos()
        for segment in snake_1.snake[1:]:
            if snake_1.head.distance(segment.pos()) < 10:
                if score.score > score.highscore:
                    score.update_highscore()
                score.game_over()
                time.sleep(1)
                snake_1.reset_snake()
                score.reset_score()
                canvas.update()

        # Detect collision with food
        if snake_1.head.distance(food.pos()) < 15:
            food.refresh()
            snake_1.add_piece()
            score.add_score()

        # Detect collision with wall
        if snake_1.head.ycor() > TOP_BORDER \
                or snake_1.head.ycor() < BOTTOM_BORDER \
                or snake_1.head.xcor() < LEFT_BORDER \
                or snake_1.head.xcor() > RIGHT_BORDER:
            if score.score > score.highscore:
                score.update_highscore()
            score.game_over()
            snake_1.snake.clear()
            time.sleep(1)
            snake_1.reset_snake()
            score.reset_score()
            canvas.update()


            #game_is_on = False






main_game_loop()
canvas.exitonclick()