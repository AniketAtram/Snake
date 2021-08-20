from turtle import Screen
from Snake import Snake
from Food import Food
from Socreboard import Scoreboard
import time
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)
screen.listen()
screen.tracer(0)
delay_time = 0.1
snake = Snake()
food = Food()
score = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(screen.bye, "Escape")

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(delay_time)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    # detect collision with tail
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (snake.head.xcor() < -280):
        is_game_over = True
        score.game_over()

    # detect collision with tali
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_over = True
            score.game_over()

print(f"Your final score was : {score.score}")

# screen.exitonclick()
